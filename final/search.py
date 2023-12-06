from flask import redirect, request, url_for, render_template, flash
from flask.views import MethodView
from google.cloud import vision
import tempfile
import os


class Search(MethodView):
    # supported image file extensions
    IMAGE_EXTENSIONS = ["jpg", "jpeg", "png", "gif", "bmp", "tiff"]
    # temporary image directory
    TMP_IMAGE_DIR = "static/tmp_image"

    def post(self):
        file = request.files["file"]

        if not self.isValidImageFile(file):
            return redirect(url_for("index"))

        image_path = self.saveImage(file)

        client = vision.ImageAnnotatorClient()

        with open(image_path, "rb") as image_file:
            content = image_file.read()

        image = vision.Image(content=content)
        labels = client.label_detection(image=image).label_annotations
        objects = client.object_localization(image=image).localized_object_annotations
        # TODO: also grab product search results to add more specificity to poem

        return redirect(
            url_for("poem", image_path=image_path, labels=labels, objects=objects)
        )

    def isValidImageFile(self, file) -> bool:
        """Returns True if the file is a valid image file, False otherwise"""
        if file.filename == "":
            flash("No file selected for uploading")
            return False
        if file.filename.split(".")[-1].lower() not in self.IMAGE_EXTENSIONS:
            flash("Invalid image file extension")
            flash("Supported image file extensions: {}".format(self.IMAGE_EXTENSIONS))
            return False
        return True

    def saveImage(self, file):
        """Saves the image file to the temporary image directory and returns the path to the image file"""
        # create temporary image directory if it doesn't exist
        if not os.path.exists(self.TMP_IMAGE_DIR):
            os.mkdir(self.TMP_IMAGE_DIR)
        # remove all image files in the temporary directory
        for filename in os.listdir(self.TMP_IMAGE_DIR):
            if filename.split(".")[-1].lower() in self.IMAGE_EXTENSIONS:
                os.remove(os.path.join(self.TMP_IMAGE_DIR, filename))
        # save the current image
        image_path = os.path.join(self.TMP_IMAGE_DIR, file.filename)
        file.save(image_path)
        return image_path

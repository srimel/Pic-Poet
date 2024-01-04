import base64
import io
import os
import pdfkit

from flask import redirect, request, send_file
from flask.views import MethodView
from pdfkit.configuration import Configuration


class Download(MethodView):
    def get(self):
        image_path = request.args.get("image_path")
        poem = request.args.get("poem")
        title = request.args.get("title")

        poem = poem.replace("\n", "<br>")

        # Create HTML format for PDF
        html = f"""
        <html>
        <body style="text-align: center;">
        <h1>Pic Poem</h1>
        <img src="data:image/png;base64,{self.image_to_base64(image_path)}" style="width: 30%; height: auto;" />
        <h2>{title}</h2>
        <p>{poem}</p>
        </body>
        </html>
        """

        wkhtmltopdf_path = os.environ.get("WKHTMLTOPDF_PATH", None)
        if wkhtmltopdf_path is not None:
            config = Configuration(wkhtmltopdf=wkhtmltopdf_path)
            pdf = pdfkit.from_string(html, False, configuration=config)
        else:
            pdf = pdfkit.from_string(html, False)

        # Create a BytesIO object from the PDF
        pdf_io = io.BytesIO(pdf)

        return send_file(
            pdf_io,
            mimetype="application/pdf",
            as_attachment=True,
            download_name="Pic-Poem.pdf",
        )

    def image_to_base64(self, image_path):
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode("utf-8")

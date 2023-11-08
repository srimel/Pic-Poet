from flask import redirect, request, url_for, render_template
from flask.views import MethodView
import qmodel


class Quote(MethodView):
    def get(self):
        return render_template("quote.html")

    def post(self):
        """
        Accepts POST requests, and processes the form;
        Redirect to the index when completed.
        """
        model = qmodel.get_model()
        model.insert(
            request.form["quote"],
            request.form["author"],
            request.form["date"],
            request.form["type"],
            request.form["source"],
            request.form["rating"],
        )
        return redirect(url_for("index"))

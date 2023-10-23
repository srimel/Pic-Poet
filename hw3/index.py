from flask import render_template
from flask.views import MethodView
import qmodel


class Index(MethodView):
    def get(self):
        model = qmodel.get_model()
        quotes = [
            dict(
                quote=row[0],
                author=row[1],
                date=row[2],
                type=row[3],
                source=row[4],
                rating=row[5],
            )
            for row in model.select()
        ]
        return render_template("index.html", quotes=quotes)

import os
import flask
from flask.views import MethodView
from index import Index
from search import Search
from poem import Poem
from download import Download

app = flask.Flask(__name__)
app.secret_key = os.environ["APP_SECRET_KEY"]

app.add_url_rule("/", view_func=Index.as_view("index"), methods=["GET"])
app.add_url_rule("/search", view_func=Search.as_view("search"), methods=["POST"])
app.add_url_rule("/poem", view_func=Poem.as_view("poem"), methods=["GET"])
app.add_url_rule("/download", view_func=Download.as_view("download"), methods=["GET"])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

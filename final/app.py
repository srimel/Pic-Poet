import flask
from flask.views import MethodView
from index import Index
from search import Search

app = flask.Flask(__name__)

app.add_url_rule("/", view_func=Index.as_view("index"), methods=["GET"])
app.add_url_rule("/search", view_func=Search.as_view("search"), methods=["POST"])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

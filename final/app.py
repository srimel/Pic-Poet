import flask
from flask.views import MethodView
from index import Index

app = flask.Flask(__name__)

app.add_url_rule("/", view_func=Index.as_view("index"), methods=["GET"])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

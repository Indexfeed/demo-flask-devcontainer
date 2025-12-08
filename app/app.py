import os

from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello, DevContainer!"


if __name__ == "__main__":
    debug_mode = os.getenv("FLASK_DEBUG", "false").lower() == "true"
    app.run(host="127.0.0.1", port=5020, debug=debug_mode)

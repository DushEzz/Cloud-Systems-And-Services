import argparse

from flask import (
    Flask,
    Response,
)


app = Flask(__name__)


@app.get("/")
def index() -> Response:
    return Response(f"Hello, {app.config['say_hello_to']}!")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--say-hello-to", default="Pelmeshki")

    return parser.parse_args()


def configure_app() -> None:
    args = parse_args()
    app.config["say_hello_to"] = args.say_hello_to


def run_app() -> None:
    configure_app()
    app.run(host="0.0.0.0", port=5000)


if __name__ == '__main__':
    run_app()

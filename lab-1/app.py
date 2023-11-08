import argparse
import os

import psycopg2
from flask import (
    Flask,
    Response,
)


app = Flask(__name__)


def increment_requests_count() -> None:
    with psycopg2.connect(
            database=os.getenv("POSTGRES_DB"),
            user=os.getenv("POSTGRES_USER"),
            password=os.getenv("POSTGRES_PASSWORD"),
            host=os.getenv("POSTGRES_HOST"),
    ) as connection:
        with connection.cursor() as cursor:
            cursor.execute("UPDATE counter SET requests_count = requests_count + 1;")


@app.get("/")
def index() -> Response:
    increment_requests_count()

    return Response(f"Hello, {app.config['say_hello_to']}!")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--say-hello-to", default="Pelmeshki")

    return parser.parse_args()


def create_app() -> Flask:
    args = parse_args()
    app.config["say_hello_to"] = args.say_hello_to

    return app


def run_app() -> None:
    app = create_app()
    app.run(host="0.0.0.0", port=5000)


if __name__ == '__main__':
    run_app()

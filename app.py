from flask import Flask
from webargs import fields
from webargs.flaskparser import use_args

from application.services import print_output
from application.services.json_handler import print_astros_number
from application.services.user_generator import generate_users
from application.services.csv_processor import CsvProcessor

# For phonebook
from application.services.phone_book import (
    create_table,
    add_item,
    read_all
)
from application.services.phone_book.db_manager import DBConnection

app = Flask(__name__)


@app.route("/get-content")
def print_file(file_name="some_input.txt") -> str | None:
    # Handle input - start.
    file_to_print = file_name
    # Handle input - end.

    # Handle logic - start.
    output = print_output(file_to_print)
    # Handle logic - end.

    return output


@app.route("/generate-users")
@use_args({"amount": fields.Int(missing=20)}, location="query")
def users_generate(args) -> str:
    # Handle input - start.
    amount = args["amount"]
    # Handle input - end.

    # Handle logic - start.
    users = generate_users(amount=amount)
    # Handle logic - end.

    users_formatted = []

    for user in users:
        user_formatted = (
            f"<li><span>{user.name}</span> - <span>{user.email}</span></li>"
        )
        users_formatted.append(user_formatted)

    item = "".join(users_formatted)
    return f"<ul>{item}</ul>"


@app.route("/space")
def get_astros() -> str | None:
    # Handle input - start.
    number_to_print = print_astros_number()
    # Handle input - end.

    return number_to_print


@app.route("/mean")
def get_mean() -> str:
    # Handle input - start.
    csv_processor = CsvProcessor()
    # Handle input - end.

    # Handle logic - start.
    string_to_print = csv_processor.get_csv_data()
    # Handle logic - end.

    return string_to_print


@app.route("/item/add")
@use_args(
    {
        "name": fields.Str(required=True),
        "number": fields.Str(required=True)
    },
    location="query"
)
def phonebook_user_add(args):

    add_item(args)

    return "OK"


@app.route("/item/read-all")
def phonebook_read_all():
    return read_all()


@app.route("/item/read/<int:pk>")
def phonebook_read_item(pk: int):
    with DBConnection() as connection:
        item = connection.execute(
            "SELECT * FROM phone_book WHERE (pk=:pk);",
            {
                "pk": pk,
            }
        ).fetchone()

    return f'{item["pk"]}: {item["name"]} - {item["number"]}'


# Create db on app run
create_table()

if __name__ == "__main__":
    app.run()

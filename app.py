# For web
from flask import (
    Flask,
    Response
)
from webargs import fields
from webargs.flaskparser import use_args

# For input/output services
from application.services import print_output
from application.services.json_handler import print_astros_number
from application.services.user_generator import generate_users
from application.services.csv_processor import CsvProcessor

# For phonebook service
from application.services.phone_book import (
    create_table,
    add_item,
    read_all,
    delete_item,
    read_item,
    update_item
)

app = Flask(__name__)


# For input/output services
# To get some output from file
@app.route("/get-content")
def print_file(file_name="some_input.txt") -> str | None:
    # Handle input - start.
    file_to_print = file_name
    # Handle input - end.

    # Handle logic - start.
    output = print_output(file_to_print)
    # Handle logic - end.

    return output


# To generate users
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


# To count astronauts
@app.route("/space")
def get_astros() -> str | None:
    # Handle input - start.
    number_to_print = print_astros_number()
    # Handle input - end.

    return number_to_print


# To get mean from data
@app.route("/mean")
def get_mean() -> str:
    # Handle input - start.
    csv_processor = CsvProcessor()
    # Handle input - end.

    # Handle logic - start.
    string_to_print = csv_processor.get_csv_data()
    # Handle logic - end.

    return string_to_print


# For phonebook application
# Add item to phonebook
@app.route("/item/add")
@use_args(
    {
        "name": fields.Str(required=True),
        "number": fields.Str(required=True)
    },
    location="query"
)
def phonebook_user_add(args: dict[fields.Str])->str:
    add_item(args)

    return "OK"


# Read all items from phonebook
@app.route("/item/read-all")
def phonebook_read_all()->str:
    return read_all()


# Read item from phonebook
@app.route("/item/read/<int:pk>")
def phonebook_read_item(pk: int)->str:
    item = read_item(pk)

    return f'{item["pk"]}: {item["name"]} - {item["number"]}'


# Update item from phonebook
@app.route("/item/update/<int:pk>")
@use_args(
    {
        "name": fields.Str(), "number": fields.Str()
    },
    location="query"
)
def item_update(args: dict[str], pk: int)->str | Response:
    result = update_item(args, pk)

    return result if result is not None else "OK"


# Delete item from phonebook
@app.route("/item/delete/<int:pk>")
def phonebook_delete_item(pk: int)->str:
    delete_item(pk)

    return "OK"


# Create db on app run
create_table()

if __name__ == "__main__":
    app.run()

from flask import Flask
from webargs import fields
from webargs.flaskparser import use_args

from application.services.user_generator import generate_users

app = Flask(__name__)


# @app.route('/')
# def hello_world():
#     return 'Hello World!'
#
#
# @app.route('/hello')
# def hello():
#     return 'Hello!'


# @app.route('/hi/<name>/<int:age>')
# @app.route('/hi/<name>')
# def hi(name: str, age: int = 42):
#     message = f'Hello {name}, age {age}.'
#
#     return message


# @app.route('/hello')
# @use_args({'name': fields.Str(missing='Bob'), 'age': fields.Int(missing=42)}, location='query')
# def hi(args):
#     name = args['name']
#     age = args['age']
#
#     return generate_message(name, age)


@app.route("/users/generate")
@use_args({"amount": fields.Int(missing=20)}, location="query")
def users_generate(args):
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


if __name__ == "__main__":
    app.run()

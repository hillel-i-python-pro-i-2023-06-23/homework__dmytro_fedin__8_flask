from flask import Flask
from webargs import fields
from webargs.flaskparser import use_args

from application.services.generate_message import generate_message

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


@app.route('/hello')
@use_args({'name': fields.Str(missing='Bob'), 'age': fields.Int(missing=42)}, location='query')
def hi(args):
    name = args['name']
    age = args['age']

    return generate_message(name, age)


if __name__ == '__main__':
    app.run()

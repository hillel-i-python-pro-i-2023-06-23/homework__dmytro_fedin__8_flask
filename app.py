from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/hello')
def hello():
    return 'Hello!'


@app.route('/hi/<name>/<int:age>')
@app.route('/hi/<name>')
def hi(name: str, age: int = 42):
    message = f'Hello {name}, age {age}.'

    return message


if __name__ == '__main__':
    app.run()

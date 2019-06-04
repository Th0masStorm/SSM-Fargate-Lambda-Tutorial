from flask import Flask
import os
app = Flask(__name__)


@app.route('/')
def hello():
    value = os.getenv('VALUE')
    return "Hello! My value is {}".format(value)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port='5000')

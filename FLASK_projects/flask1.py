from flask import Flask
import random

app = Flask(__name__)

print(random.__name__)
print(__name__)

@app.route('/')

def hello_world():
    return ' <h1 style="text-align: center"> Hello, World! </h1><p>This is a paragraph. </p>'
    

@app.route("/bye")
def bye():
    return "Bye!"

@app.route("/<name>")
def greet(name):
    return f"Hello there {name}"


if __name__ == "__main__":
    app.run(debug=True)

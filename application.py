from flask import Flask
app = Flask(__name__)

@app.route("/welcome/<username>")
def welcome(username):
    

    return f"Welcome, {username}"

@app.route("/hello/")
def hello():
    return "Hello World"

@app.route("/hey")
def hey():
    return "Hey Man"


if __name__ == "__main__":
    app.run(debug = True)

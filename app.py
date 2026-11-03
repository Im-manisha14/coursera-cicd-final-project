from flask import Flask


app = Flask(__name__)


@app.get("/")
def home():
    """Return the application's welcome message."""
    return "Welcome to the Coursera CI/CD Final Project!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

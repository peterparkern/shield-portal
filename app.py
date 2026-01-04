from flask import Flask, render_template, send_file
import os

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/admin")
def admin():
    return render_template("admin.html")


@app.route("/robots.txt")
def robots():
    return (
        """User-agent: *
Disallow: /admin""",
        200,
        {"Content-Type": "text/plain"},
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

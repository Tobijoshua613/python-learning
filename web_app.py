# 🌐 Simple Python Web App
# Flask Practice Project

from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return """
    <h1>🚀 Welcome to My Python Web App</h1>
    <p>I am learning Python and AI Engineering.</p>
    <p>This website was built with Flask.</p>
    """


@app.route("/about")
def about():
    return """
    <h1>About Me</h1>
    <p>I am building my skills in Python, APIs, databases, and AI.</p>
    """


@app.route("/projects")
def projects():
    return """
    <h1>My Python Projects</h1>

    <ul>
        <li>Expense Tracker</li>
        <li>Currency Converter</li>
        <li>Country Information API</li>
        <li>Student Database</li>
        <li>Contact Book</li>
    </ul>
    """


if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


expenses = []


@app.route("/expense-tracker", methods=["GET", "POST"])
def expense_tracker():

    if request.method == "POST":

        name = request.form["name"]
        amount = float(request.form["amount"])
        category = request.form["category"]

        expenses.append({
            "name": name,
            "amount": amount,
            "category": category
        })

    total = sum(expense["amount"] for expense in expenses)

    return render_template(
        "expense_tracker.html",
        expenses=expenses,
        total=total
    )


if __name__ == "__main__":
    app.run(debug=True)

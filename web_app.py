from flask import Flask, render_template
import sqlite3

app = Flask(__name__) 

DATABASE = "expenses.db"


def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db()

    conn.execute("""
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            amount REAL NOT NULL,
            category TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()
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

from flask import Flask, render_template, request, redirect
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


@app.route("/expense-tracker", methods=["GET", "POST"])
def expense_tracker():

    if request.method == "POST":
        name = request.form["name"]
        amount = float(request.form["amount"])
        category = request.form["category"]

        conn = get_db()

        conn.execute(
            """
            INSERT INTO expenses (name, amount, category)
            VALUES (?, ?, ?)
            """,
            (name, amount, category)
        )

        conn.commit()
        conn.close()

        return redirect("/expense-tracker")

    conn = get_db()

    expenses = conn.execute(
        "SELECT * FROM expenses ORDER BY id DESC"
    ).fetchall()

    total = conn.execute(
        "SELECT COALESCE(SUM(amount), 0) FROM expenses"
    ).fetchone()[0]

    conn.close()

    return render_template(
        "expense_tracker.html",
        expenses=expenses,
        total=total
    )


@app.route("/")
def home():
    return render_template("index.html")


if __name__ == "__main__":
    init_db()
    app.run(debug=True)

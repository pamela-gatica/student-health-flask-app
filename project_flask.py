from flask import Flask, render_template
import sqlite3
import pathlib

base_path = pathlib.Path(__file__).parent
db_path = base_path / "student_health_data.db"

app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn


@app.route("/")
def homepage():
    return render_template("homepage.html")


@app.route("/about")
def about_page():
    return render_template("about.html")


@app.route("/data")
def data_page():
    try:
        conn = get_db_connection()
        students = conn.execute("""
            SELECT *
            FROM student_health
            LIMIT 100
        """).fetchall()
        conn.close()

        return render_template("data_table.html", students=students)

    except sqlite3.Error as e:
        return f"Database error: {e}", 500


@app.route("/group")
def group_info():
    return render_template("group_info.html")


if __name__ == "__main__":
    app.run()

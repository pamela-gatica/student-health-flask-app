from flask import Flask, render_template, request
import sqlite3
import pathlib
import math
import pandas as pd

from dashboard import build_dashboard, build_insights

base_path = pathlib.Path(__file__).parent
db_path = base_path / "student_health_data.db"

app = Flask(__name__)

PER_PAGE = 25

# Maps URL query param names to the columns they filter on
FILTER_FIELDS = {
    "gender": "Gender",
    "activity": "Physical_Activity",
    "sleep": "Sleep_Quality",
    "mood": "Mood",
    "risk": "Health_Risk_Level",
}


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

        # Build the WHERE clause from any filters present in the query string
        filters = {}
        where_clauses = []
        params = []
        for param, column in FILTER_FIELDS.items():
            value = request.args.get(param, "").strip()
            if value:
                filters[param] = value
                where_clauses.append(f"{column} = ?")
                params.append(value)
        where_sql = f"WHERE {' AND '.join(where_clauses)}" if where_clauses else ""

        total = conn.execute(
            f"SELECT COUNT(*) FROM student_health {where_sql}", params
        ).fetchone()[0]
        total_pages = max(1, math.ceil(total / PER_PAGE))

        page = request.args.get("page", 1, type=int)
        page = max(1, min(page, total_pages))
        offset = (page - 1) * PER_PAGE

        students = conn.execute(f"""
            SELECT *
            FROM student_health
            {where_sql}
            ORDER BY Student_ID
            LIMIT ? OFFSET ?
        """, params + [PER_PAGE, offset]).fetchall()

        # Distinct values to populate each filter dropdown
        filter_options = {
            param: [
                row[0] for row in
                conn.execute(f"SELECT DISTINCT {column} FROM student_health ORDER BY {column}").fetchall()
            ]
            for param, column in FILTER_FIELDS.items()
        }

        conn.close()

        start = offset + 1 if total else 0
        end = min(offset + PER_PAGE, total)

        return render_template(
            "data_table.html",
            students=students,
            page=page,
            total_pages=total_pages,
            total=total,
            start=start,
            end=end,
            filters=filters,
            filter_options=filter_options,
        )
    except sqlite3.Error as e:
        return f"Database error: {e}", 500


@app.route("/dashboard")
def dashboard_page():
    try:
        conn = get_db_connection()
        df = pd.read_sql_query("SELECT * FROM student_health", conn)
        conn.close()

        charts = build_dashboard(df)
        return render_template("dashboard.html", charts=charts, total=len(df))
    except sqlite3.Error as e:
        return f"Database error: {e}", 500


@app.route("/insights")
def insights_page():
    try:
        conn = get_db_connection()
        df = pd.read_sql_query("SELECT * FROM student_health", conn)
        conn.close()

        insights = build_insights(df)
        return render_template("insights.html", insights=insights, total=len(df))
    except sqlite3.Error as e:
        return f"Database error: {e}", 500


@app.route("/group")
def group_info():
    return render_template("group_info.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)

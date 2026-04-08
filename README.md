# Student Health Data Web App

## Overview
A lightweight Flask-based web application that integrates SQLite to explore and analyze student health and wellness data. The application provides an intuitive interface to view key indicators such as stress levels, sleep quality, physical activity, mood, and overall health risk.

This project demonstrates how to build a simple end-to-end data application combining backend development, database management, and web visualization.

Contents
1. [Project Name](#project-name)
2. [Project Description](#project-description)
3. [Prerequisites and Packages/Libraries](#prerequisites-and-packageslibraries)
4. [Getting Started](#getting-started)
5. [Installation and Configuration Instructions](#installation-and-configuration-instructions)
6. [Running the project_flask Application](#running-the-project_flask-application)
7. [Project/Code Structure](#projectcode-structure)
8. [App Routes](#app-routes)
9. [License](#license)
10. [References](#references)
9. [Contributing](#contributing)
10. [Authors and Contributors](#authors-&-contributors)
12. [License](#license)
13. [References](#references)
14. [Additional Information](#additional-information)

## Features
- Web application built with Flask
- Integration with SQLite database
- Multiple navigation pages using HTML templates
- Displays structured student health data
- Clean and simple user interface
- Modular and maintainable code structure

## Dataset

The dataset contains student health and lifestyle indicators, including:

- Age and Gender
- Heart Rate
- Blood Pressure (Systolic & Diastolic)
- Stress Level (Biosensor & Self-Report)
- Physical Activity
- Sleep Quality
- Mood
- Study Hours
- Project Hours
- Health Risk Level

Source: [Kaggle - Student Health Data](https://www.kaggle.com/datasets/ziya07/student-health-data)

## Tech Stack
- Python
- Flask
- SQLite
- HTML / Jinja Templates
- Pathlib

## Project Structure
```
student-health-flask-app/
│
├── app.py
├── student_health_data.db
├── requirements.txt
├── README.md
│
├── templates/
│   ├── homepage.html
│   ├── about.html
│   ├── data_table.html
│   └── group_info.html
│
└── static/
    └── style.css
```

## Application Routes
```
| Route    | Description                     |
| -------- | ------------------------------- |
| /        | Homepage                        |
| /about   | Dataset and project description |
| /data    | Displays student health data    |
| /group   | Contributors information        |
```

## Installation & Setup
1. Clone the repository:
   ```
   git clone https://github.com/your-username/student-health-flask-app.git
   cd student-health-flask-app
   ```
3. Create virtual environment (optional but recommended):
4. Install dependencies:
5. Run the application:
6. Open in browser:

## Prerequisites and Packages/Libraries
- Python 3.12.7
- Flask and `render_template` from flask
- SQLite3
- Pathlib
## Getting Started
- Develop Python codes:
  - SQL Database and Table using `sqlite3`
  - `project_flask` website
- Develop HTML codes and save in a folder named `template`:
  - Homepage
  - About page
  - Data page
  - Group Information
## Installation and Configuration Instructions
- Use the virtual environment (myspace) created in Visual Studio Code.
- Install and import the required packages:
  - `pip install flask` and import `Flask`, `render_template`
  - Import `sqlite3`, `pathlib`
- Setup the database: Ensure you have the `student_health_data.db` SQLite database in the project directory. If not, create and populate it accordingly.
- Define codes for the `project_flask` for the website:
  - `app_routes` for the four HTML files (homepage, about, data_table, group_info)
  - Path to call the database `student_health_data.db`
  - `app.run` to run the code
## Running the project_flask Application
1. Start the `project_flask` app by executing the code for the application:
    ```bash
    # Serving Flask app 'project_flask'
    # Debug mode: on
    WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
    # Running on http://127.0.0.1:5000
    Press CTRL+C to quit
    # Restarting with stat
    # Debugger is active!
    # Debugger PIN: 696-082-221
    ```
2. Access the application:
    - Open a web browser and go to [http://127.0.0.1:5000/](http://127.0.0.1:5000/)
    - This opens the `project_flask` website
## Project/Code Structure
1. `project_flask.py`: The main Flask application file.
2. `templates/`: Directory containing HTML files.
   - `homepage.html`: The project information page.
   - `about.html`: The about page is the information about the dataset, describing the functions of each variable.
   - `data_table.html`: The page displaying the sample of 100 observations in the student health data.
   - `group_info.html`: Names and IDs of group 10 members
## App Routes
1. `/`: Displays the project information page.
2. `/about`: Displays the about page.
3. `/data`: Connects to the SQLite database, retrieves student health data, and displays it in a table.
4. `/group_info`: Displays the names of the group 10 members
## Contributing
All 4 members of group 10 contributed imensely to make this project a success, kudos to a good job done.
We also want to thank our lecturer, Professor Simranjeet, for the knowledge she impacted on us, that has enabled us to successfully develop this project. We appreciate all your kind assistance. 
## Authors & contributors
The list of all 4 members of Group 10 who contributed to the project is detailed in the group_info page.
## License
The `flask_project` is the final group project for the Introduction to Python Programming (DAB 111) course under the St. Clair Data Analytics for Business Program.
## References
- Flask documentation: [Flask Docs](https://flask.palletsprojects.com/)
- SQLite documentation: [SQLite Docs](https://www.sqlite.org/docs.html)
- HTML documentation: [HTML Docs](https://www.w3schools.com/html/)
- Dataset Source: [Kaggle - Student Health Data](https://www.kaggle.com/datasets/ziya07/student-health-data)
- Lecture notes


  
## Additional Information:
- The requirements document for the project_flask (Student Health Data) Flask Application. This document provides the key points to ensure project_flask runs smoothly


Functional Requirements:

1. Application Setup

- Install Flask, SQLite3, and other dependencies.
- Use pathlib for dynamic path management.
- Define the SQLite database file relative to the script’s directory.

2. Homepage

- Route: /
- Functionality: Render homepage.html and provide navigation to other sections.

3. About Page

- Route: /about
- Functionality: Render about.html with an overview of the dataset and application purpose.

4. Data Page

- Route: /data
- Functionality: Connect to the SQLite database, fetch records from student_health, and render data_table.html.

5. Group Information Page

- Route: /group
- Functionality: Render group_info.html with information about health groups.


Non-Functional Requirements:

1. Usability

- Ensure responsive and user-friendly web pages.
- Use well-styled HTML templates.

2. Performance

- Optimize database queries for efficiency.
- Ensure fast navigation between pages.

3. Portability

- Ensure the application runs on all major platforms.
- Use pathlib for cross-platform compatibility.

4. Maintainability

- Follow a clear code structure.
- Use comments and descriptive function names.

5. Security

- Use parameterized queries to prevent SQL injection.
- Avoid exposing sensitive data during debugging.


Technical Requirements:

1. Software Dependencies

- Python 3.8 or later.
- Required libraries: Flask, SQLite3, Pathlib.

2. Directory Structure

- app.py (Main application file)
- templates/ (HTML templates directory)
* homepage.html
* about.html
* data_table.html
*group_info.html

- static/ (Directory for CSS, JS, and images)
- student_health_data.db (SQLite database file)

3. Database Schema

- SQLite database: student_health_data.db
- Table: student_health
* Columns(14): [ Student_ID, Age, Gender, Heart_Rate, Blood_Pressure_Systolic, Blood_Pressure_Diastolic, Stress_Level_Biosensor, Stress_Level_Self_Report, Physical_Activity, Sleep_Quality, Mood, Study_Hours, Project_Hours, Health_Risk_Level ]


Example Use Case:
- Homepage: User gets a welcome message and sees navigation links to other sections for additional information about the project.
- About Page: User reads an overview of the dataset.
- Data Page: User views student health data entered in the data_table.
- Group Information Page: User sees the names and ID numbers of the group members who worked on the project_flask.


Testing Requirements:
- Unit tests for route responses.
- Functional tests for database connection and data retrieval.
- Integration tests to verify template rendering.

Code Implementation:
- Here's a brief overview of the project_flask code and recommendations for running it in some python environments:
[
from flask import Flask, render_template
import sqlite3
import pathlib

base_path = pathlib.Path(__file__).parent
db_name = "student_health_data.db"
db_path = base_path / db_name

app = Flask(__name__)

@app.route("/")
def homepage():
return render_template("homepage.html")

@app.route("/about")
def about_page():
return render_template("about.html")

@app.route("/data")
def data_page():
con = sqlite3.connect(db_path)
cursor = con.cursor()
students = cursor.execute("SELECT * FROM student_health").fetchall()
con.close()
return render_template("data_table.html", students=students)

@app.route("/group")
def group_info():
return render_template("group_info.html")

if __name__ == "__main__":
app.run(debug=True)
]

Recommendations for Code Execution:
- Ensure you have the necessary dependencies installed within the particular environment
- Use %run project_flask.py to run the Flask app within the notebook
- Use python project_flask.py to run the Flask within VSCode terminal
- Make sure your HTML templates are in the correct directory.

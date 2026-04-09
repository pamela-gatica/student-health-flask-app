# Student Health Data Web App

## Overview
A lightweight Flask-based web application that integrates SQLite to explore and analyze student health and wellness data. The application provides an intuitive interface to view key indicators such as stress levels, sleep quality, physical activity, mood, and overall health risk.

This project demonstrates how to build a simple end-to-end data application combining backend development, database management, and web visualization.

## Application Preview
![Homepage](images/home.png)
![Data Table](images/data.png)

Contents
- [Features](#features)
- [Dataset](#dataset)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Application Routes](#application-routes)
- [Installation & Setup](#installation--setup)
- [Key Learning Outcomes](#key-learning-outcomes)
- [Future Improvements](#future-improvements)

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
├── templates/
│   ├── about.html
│   ├── base.html
│   ├── data_table.html
│   ├── homepage.html
│   └── group_info.html
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
### 1. Clone the repository:
   ```
   git clone https://github.com/your-username/student-health-flask-app.git
   cd student-health-flask-app
   ```
### 2. Create virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate   # Mac/Linux
   venv\Scripts\activate      # Windows
   ```
### 3. Install dependencies:
    pip install flask
### 4. Run the application:
    python app.py
### 5. Open in browser:
    http://127.0.0.1:5000/

## Key Learning Outcomes
- Building a web application using Flask
- Connecting Python applications to an SQLite database
- Structuring a multi-page web app with templates
- Handling and displaying structured data
- Writing clean and maintainable backend code

## Future Improvements
- Add filtering options (by gender, mood, health risk level)
- Implement pagination for large datasets
- Add data visualizations (charts and dashboards)
- Improve UI/UX design with CSS frameworks
- Deploy the application (e.g., Render, Railway, or Heroku)

## Author
Pamela Gatica

Data Analytics Student | Background in Psychology & HR

## Final Note
This project is part of my journey into data analytics and backend development, focusing on transforming raw data into accessible and meaningful insights through simple web applications.

# Student Health Data Web App

## Overview
A lightweight Flask-based web application that integrates SQLite to explore and analyze student health and wellness data. The application provides an intuitive interface to view key indicators such as stress levels, sleep quality, physical activity, mood, and overall health risk.

This project highlights the integration of data analytics concepts with web development to deliver accessible and interactive data exploration.

## Application Preview
<img src="images/home.png" width="700">
<img src="images/data.png" width="700">

## Data Files
- `student_health_data.csv`: Raw dataset used for data ingestion and preprocessing  
- `student_health_data.db`: SQLite database used by the Flask application  
- `project.ipynb`: Jupyter Notebook used for data cleaning, preprocessing, and exploratory data analysis (EDA), forming the foundation for the web application  

Contents
- [Features](#features)
- [Dataset](#dataset)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Application Routes](#application-routes)
- [Installation & Setup](#installation--setup)
- [Project Evolution](#project-evolution)
- [Key Learning Outcomes](#key-learning-outcomes)
- [Key Highlights](#key-highlights)
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
- HTML / Jinja2 Templates
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
## Application Routes

| Route  |           Description           |
|--------|---------------------------------|
| /      | Homepage                        |
| /about | Dataset and project description |
| /data  | Displays student health data    |
| /group | Contributors information        |
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
    pip install -r requirements.txt
### 4. Run the application:
    python app.py
### 5. Open in browser:
    http://127.0.0.1:5000/

## Project Evolution
This project was initially developed as a collaborative academic assignment. 
It has since been independently enhanced and transformed into a portfolio project by Pamela Gatica, 
including improvements in:

- Code structure and organization  
- UI/UX design and styling  
- Documentation and project presentation  
- Application maintainability and scalability  

## Key Learning Outcomes
- Building a web application using Flask
- Connecting Python applications to an SQLite database
- Structuring a multi-page web app with templates
- Handling and displaying structured data
- Writing clean and maintainable backend code

## Key Highlights
- End-to-end data application using Python and Flask  
- Integration of structured datasets with a relational database  
- Clean UI design for improved data accessibility  
- Transformation of an academic project into a professional portfolio piece  

## Future Improvements
- Add filtering options (by gender, mood, health risk level)
- Implement pagination for large datasets
- Add data visualizations (charts and dashboards)
- Improve UI/UX design with CSS frameworks
- Deploy the application (e.g., Render, Railway, or Heroku)

## Author

**Pamela Gatica**  
Data Analytics Student | Background in Psychology & HR  

- Interested in data analytics, backend development, and data-driven applications  
- Currently building portfolio projects combining Python, data, and web development  
## Final Note
This project is part of my journey into data analytics and backend development, focusing on transforming raw data into accessible and meaningful insights through simple web applications.

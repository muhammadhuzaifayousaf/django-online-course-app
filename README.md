# Django Online Course App

A Django-based online course application with course management, lessons, quizzes, user authentication, and exam results.

## Features

- Course and lesson management
- Instructor and learner management
- Quiz questions and choices
- Online exam submission
- Automatic score calculation
- Exam result display
- Django Admin panel
- Bootstrap-based UI

## Technologies

- Python
- Django
- SQLite
- HTML/CSS
- Bootstrap

## Installation

```bash
git clone https://github.com/muhammadhuzaifayousaf/django-online-course-app.git
cd django-online-course-app

python -m venv venv
venv\Scripts\activate

pip install django
python manage.py migrate
python manage.py runserver
````

Open:

```text
http://127.0.0.1:8000/
```

## Main Models

* Course
* Instructor
* Learner
* Lesson
* Question
* Choice
* Submission

## Exam System

Learners can attempt course exams, submit their answers, and view their score and correct answers.

## Admin

The Django Admin panel can be used to manage courses, lessons, questions, choices, instructors, learners, and submissions.

# Ad Budget Management System

This project is a Django + Celery-based backend system that helps manage advertising budgets for brands. Each brand can have multiple campaigns with daily and monthly budgets. The system automatically tracks spending, enforces budget limits, and manages campaign status based on dayparting schedules.

## Features

- Track daily and monthly spend per campaign
- Automatically pause campaigns that exceed their budget
- Resume eligible campaigns at the start of a new day or month
- Enforce campaign schedules using dayparting (allowed hours)
- Reset daily and monthly budgets automatically
- Fully statically typed with `mypy` and Django stubs

## Technology Stack

- Django (models, admin interface, business logic)
- Celery (background tasks)
- django-celery-beat (periodic task scheduling)
- Redis (Celery broker)
- PostgreSQL or SQLite (database)
- Python type hints with `mypy` and `django-stubs`

## Data Model Overview

### Brand
- `name`: string
- `daily_budget`: float
- `monthly_budget`: float

### Campaign
- `brand`: ForeignKey to Brand
- `name`: string
- `is_active`: boolean
- `dayparting_start`: time
- `dayparting_end`: time

### Spend
- `campaign`: ForeignKey to Campaign
- `date`: date
- `daily_spend`: float
- `monthly_spend`: float

## Workflow Description

### Spend Tracking
Spending is updated regularly for each campaign, tracked daily and monthly in the `Spend` model.

### Budget Enforcement (Periodic Task)
Every few minutes, a Celery task checks whether each campaign has exceeded its budget. If a campaign goes over its daily or monthly limit, it is paused.

### Dayparting Enforcement (Periodic Task)
Campaigns are only active during their allowed hours, specified by `dayparting_start` and `dayparting_end`. Outside this time range, campaigns are paused.

### Daily and Monthly Resets
- Daily spend is reset every night at midnight UTC.
- Monthly spend is reset on the first day of each month.
- Campaigns are reactivated automatically if they are within budget and within the current dayparting window.

## Setup Instructions

### Clone the Repository


git clone [url]
cd ad-budget


### Create a Virtual Environment

python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

### Install Dependencies
pip install -r requirements.txt

### Apply Migrations
python manage.py migrate

### Run the Development Server
python manage.py runserver

###  Start Redis (Locally)
Ensure Redis is running on localhost:6379.

### Start Celery and Celery Beat
In separate terminal windows:
celery -A ad_budget worker --loglevel=info
celery -A ad_budget beat --loglevel=info


Static Typing
This project uses full static typing and has passed all mypy checks.

### To run the type checker:
mypy .


### GitHub Deployment

git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin [url]
git push -u origin main
# Django + Celery Budget Management System

## Objective

A backend system for an Ad Agency to manage advertising campaigns across brands, with automated budget tracking and enforcement using Django and Celery.

## Features

- Track daily and monthly ad spend per brand
- Automatically pause/resume campaigns based on budget limits
- Reset spends daily/monthly
- Respect dayparting (campaigns only run during allowed hours)
- Background processing via Celery
- Admin panel for managing brands and campaigns

## Tech Stack

- Python 3.12
- Django 5.x
- Celery
- Redis (via Docker)
- SQLite (can be switched to PostgreSQL)
- django-celery-beat
- mypy (for static typing)

## Setup Instructions

### 1. Clone the repository

 
git clone https://github.com/Asifayub214/ad_budget.git
cd ad_budget
```

### 2. Create virtual environment and install requirements

 
python -m venv venv
venv\Scripts\activate   # Windows
pip install -r requirements.txt
```

### 3. Start Redis (via Docker)

 
docker run --name redis-budget -p 6379:6379 -d redis
```

### 4. Run migrations

 
python manage.py migrate
```

### 5. Create admin user (sample)

 
python manage.py createsuperuser
# Username: admin
# Password: admin123 (you choose)
```

### 6. Start Django server

 
python manage.py runserver
```

### 7. Start Celery worker

 
celery -A ad_budget worker --loglevel=info
```

### 8. Start Celery beat scheduler (for periodic tasks)

 
celery -A ad_budget beat --loglevel=info
```

## Data Models

- **Brand**
  - name
  - daily_budget
  - monthly_budget

- **Campaign**
  - name
  - linked to a Brand
  - active (boolean)
  - start_hour / end_hour (dayparting)
  - daily_spend / monthly_spend

## System Workflow

1. **Spend Tracking**
   - Spend is tracked per campaign and aggregated to brand level.

2. **Budget Enforcement**
   - Celery task checks if daily/monthly spend exceeds the brand’s budget.
   - Pauses campaigns that exceed budget.

3. **Dayparting**
   - Campaigns are enabled/disabled based on current hour falling within their allowed time range.

4. **Daily/Monthly Resets**
   - Spends reset to 0 at midnight/day 1 of month.
   - Inactive campaigns are reactivated if under budget and within dayparting window.

## Static Typing (mypy)

- Codebase uses full PEP 484-style type hints.
- Run checks with:

 
mypy .
```

- `mypy.ini` is configured to ignore third-party stubs.
- No `Any` is used unless necessary.

## Tests

Run unit tests:

 
python manage.py test
```

Includes:
- Basic model tests
- Dayparting logic checks

## GitHub Actions (CI)

`.github/workflows/mypy.yml` is included to run `mypy` checks automatically on each push to `main`.

## Assumptions

- Campaigns spend is simulated (not tracking real-time ad spend)
- Dayparting uses local server time
- All campaigns start with zero spend each day/month
- Redis is assumed to be available via Docker locally

## Repository

GitHub Repository: https://github.com/Asifayub214/ad_budget


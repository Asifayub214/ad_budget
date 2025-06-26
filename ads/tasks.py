from celery import shared_task
from .services import enforce_budget_limits, enforce_dayparting, reset_daily_spends, reset_monthly_spends

@shared_task
def check_budgets() -> None:
    enforce_budget_limits()

@shared_task
def enforce_dayparting_schedule() -> None:
    enforce_dayparting()

@shared_task
def daily_reset() -> None:
    reset_daily_spends()
    reset_monthly_spends()

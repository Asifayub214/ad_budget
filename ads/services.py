from .models import Campaign, Brand
from typing import List
from django.utils import timezone

def enforce_budget_limits() -> None:
    now = timezone.now()
    for campaign in Campaign.objects.select_related('brand').all():
        brand = campaign.brand
        if (campaign.daily_spend >= brand.daily_budget or
            campaign.monthly_spend >= brand.monthly_budget):
            campaign.active = False
            campaign.save()

def enforce_dayparting() -> None:
    now_hour = timezone.now().hour
    for campaign in Campaign.objects.prefetch_related('schedules'):
        if not campaign.schedules.exists():
            continue
        active = any(sch.start_hour <= now_hour < sch.end_hour for sch in campaign.schedules.all())
        if campaign.active != active:
            campaign.active = active
            campaign.save()

def reset_daily_spends() -> None:
    Campaign.objects.all().update(daily_spend=0, active=True)

def reset_monthly_spends() -> None:
    now = timezone.now()
    if now.day == 1:
        Campaign.objects.all().update(monthly_spend=0, active=True)

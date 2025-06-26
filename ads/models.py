from django.db import models
from typing import Optional
from django.utils import timezone

class Brand(models.Model):
    name = models.CharField(max_length=100)
    daily_budget = models.FloatField()
    monthly_budget = models.FloatField()

    def __str__(self) -> str:
        return self.name

class Campaign(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='campaigns')
    name = models.CharField(max_length=100)
    active = models.BooleanField(default=True)
    daily_spend = models.FloatField(default=0)
    monthly_spend = models.FloatField(default=0)

    def __str__(self) -> str:
        return self.name

class DaypartingSchedule(models.Model):
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE, related_name='schedules')
    start_hour = models.PositiveSmallIntegerField()  # 0–23
    end_hour = models.PositiveSmallIntegerField()    # 0–23

    def is_active_now(self) -> bool:
        now_hour = timezone.now().hour
        return self.start_hour <= now_hour < self.end_hour

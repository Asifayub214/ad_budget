from django.core.management.base import BaseCommand
from ads.services import reset_daily_spends, reset_monthly_spends
from typing import Any

class Command(BaseCommand):
    help = 'Resets campaign spends daily/monthly'

    def handle(self, *args: Any, **options: Any) -> None:
        reset_daily_spends()
        reset_monthly_spends()
from django.test import TestCase
from ads.models import Brand, Campaign

class CampaignModelTest(TestCase):
    def setUp(self) -> None:
        self.brand = Brand.objects.create(name="Test Brand", daily_budget=1000, monthly_budget=20000)

    def test_campaign_creation(self) -> None:
        campaign = Campaign.objects.create(
            brand=self.brand,
            name="Test Campaign"
        )
        self.assertEqual(campaign.brand, self.brand)
        self.assertEqual(campaign.name, "Test Campaign")
        self.assertTrue(campaign.active)
        self.assertEqual(campaign.daily_spend, 0)
        self.assertEqual(campaign.monthly_spend, 0)

    def test_campaign_str_method(self) -> None:
        campaign = Campaign.objects.create(brand=self.brand, name="My Campaign")
        self.assertEqual(str(campaign), "My Campaign")

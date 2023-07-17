from core.models import Property

from django.test import TestCase
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status


class PricingRuleAPITestCase(TestCase):
    def setUp(self):
        # self.url = reverse('pricing-rule')
        self.url = "/api/v1.0/pricing-rule/"
        self.client = APIClient()

        self.property = Property.objects.create(
            name="Hotel1",
            base_price=100,
        )

        return super().setUp()
    
    def test_wrong_rule(self):
        response = self.client.post(
            self.url,
            {
                "property": self.property.id,
                "min_stay_length": 0,
                "specific_day": "2023-07-17"
            },
            format='json'
        )

        # Expected to fail
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_good_rule(self):
        response = self.client.post(
            self.url,
            {
                "property": self.property.id,
                "price_modifier": 0,
                "min_stay_length": 0,
                "fixed_price": 0,
                "specific_day": "2023-07-17"
            },
            format='json'
        )

        # Expected to work
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    
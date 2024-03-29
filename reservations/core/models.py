from django.db import models


class Property(models.Model):
    """
        Model that represents a property.
        A property could be a house, a flat, a hotel room, etc.
    """
    name = models.CharField(max_length=255, blank=True, null=True)
    """name: Name of the property"""
    base_price = models.FloatField(null=True, blank=True)
    """base_price: base price of the property per day"""


class PricingRule(models.Model):
    """
        Model that represents a pricing rule that will be applied to a property when booking.
        A rule can have a fixed price, or a percent modifier.
        Only one rule can apply per day.
        We can have multiple rules for the same day, but only the most relevant rule applies.
    """
    property = models.ForeignKey('core.Property', blank=False, null=False, on_delete=models.CASCADE)
    """property: This rule is applied to a particular property"""
    price_modifier = models.FloatField(null=True, blank=True)
    """price_modifier: Represents a percentage that can be positive (increment) or negative (discount)"""
    min_stay_length = models.IntegerField(null=True, blank=True)
    """min_stay_length: This rule applies only if the stay_length of the booking is >= min_stay_length """
    fixed_price = models.FloatField(null=True, blank=True)
    """fixed_price: A rule can have a fixed price for the given day"""
    specific_day = models.DateField(null=True, blank=True)
    """specific_day: A rule can apply to a specific date. Ex: Christmas"""

    def __str__(self):
        return f"Rule for property: p {self.property_id} - price {self.price_modifier} - stay {self.min_stay_length} - fixed {self.fixed_price} - day {self.specific_day}"


class Booking(models.Model):
    """
        Model that represent a booking.
        A booking is done when a customer books a property for a given range of days.
        The booking model is also in charge of calculating the final price the customer will pay.
    """
    property = models.ForeignKey('core.Property', blank=False, null=False, on_delete=models.CASCADE)
    """property: The property this booking is for"""
    date_start = models.DateField(blank=False, null=False)
    """date_start: First day of the booking"""
    date_end = models.DateField(blank=False, null=False)
    """date_end: Last date of the booking"""
    final_price = models.FloatField(null=True, blank=True)
    """final_price: Calculated final price"""

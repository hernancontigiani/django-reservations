from core.models import Property, PricingRule, Booking
from rest_framework import serializers


class PropertySerializer(serializers.ModelSerializer):

    class Meta:
        model = Property
        fields = ('id', 'name', 'base_price')



class PricingRuleSerializer(serializers.ModelSerializer):
    property = serializers.PrimaryKeyRelatedField(queryset= Property.objects.all())

    def validate(self, data):
        """
        Check price rule condition.
        """
        if data.get('price_modifier') is None and data.get('fixed_price') is None:
            raise serializers.ValidationError(
                {
                    "price_modifier": "it cannont be null if fixed_price is null",
                    "fixed_price": "it cannont be null if price_modifier is null"
                }
            )
        return data

    class Meta:
        model = PricingRule
        fields = ('id', 'property', 'price_modifier', 'min_stay_length', 'fixed_price', 'specific_day')

    
class BookingSerializer(serializers.ModelSerializer):
    property = serializers.PrimaryKeyRelatedField(queryset= Property.objects.all())

    class Meta:
        model = Booking
        fields = ('id', 'property', 'date_start', 'date_end', 'final_price')


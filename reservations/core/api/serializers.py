from ..models import *
from rest_framework import serializers


class PropertySerializer(serializers.ModelSerializer):

    class Meta:
        model = Property
        fields = ('__all__')



class PricingRuleSerializer(serializers.ModelSerializer):
    property = serializers.PrimaryKeyRelatedField(write_only=True, queryset= Property.objects.all())

    class Meta:
        model = PricingRule
        fields = ('__all__')

    
class BookingSerializer(serializers.ModelSerializer):
    property = serializers.PrimaryKeyRelatedField(write_only=True, queryset= Property.objects.all())

    class Meta:
        model = Booking
        fields = ('__all__')
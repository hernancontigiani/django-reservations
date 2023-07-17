from core.models import Property, PricingRule, Booking
from core.api.serializers import PropertySerializer, PricingRuleSerializer, BookingSerializer
from core.api.services import *

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status


class PropertyViewSet(viewsets.ModelViewSet):
    permission_classes = [] # Pending auth
    serializer_class = PropertySerializer
    queryset = Property.objects.all()


class PricingRuleViewSet(viewsets.ModelViewSet):
    permission_classes = [] # Pending auth
    serializer_class = PricingRuleSerializer
    queryset = PricingRule.objects.all()


class BookingViewSet(viewsets.ModelViewSet):
    permission_classes = [] # Pending auth
    serializer_class = BookingSerializer
    queryset = Booking.objects.all()

    def create(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)

        # Validate JSON data and calculate final price
        if serializer.is_valid():
            data["final_price"] = calculate_final_price(serializer.validated_data)

        # Validate calculated data and save
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                data=serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            data=serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    
    
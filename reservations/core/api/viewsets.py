from ..models import *
from .serializers import *
from rest_framework import viewsets


class PropertyViewSet(viewsets.ModelViewSet):
    permission_classes = [] # Pending auth
    serializer_class = PropertySerializer
    queryset = serializer_class.Meta.model.objects.all()


class PricingRuleViewSet(viewsets.ModelViewSet):
    permission_classes = [] # Pending auth
    serializer_class = PricingRuleSerializer
    queryset = serializer_class.Meta.model.objects.all()


class BookingViewSet(viewsets.ModelViewSet):
    permission_classes = [] # Pending auth
    serializer_class = BookingSerializer
    queryset = serializer_class.Meta.model.objects.all()

    
    
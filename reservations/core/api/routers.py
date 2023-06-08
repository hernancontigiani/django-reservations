from .viewsets import *
from rest_framework.routers import DefaultRouter


router = DefaultRouter()

# Routers
router.register(r'property', viewset=PropertyViewSet, basename='property') 
router.register(r'pricing-rule', viewset=PricingRuleViewSet, basename='pricing-rule') 
router.register(r'booking', viewset=BookingViewSet, basename='booking') 


urlpatterns = router.urls
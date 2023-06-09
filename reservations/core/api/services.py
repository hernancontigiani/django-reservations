from datetime import datetime, timedelta

from ..models import *
from django.db.models import Q


def calculate_final_price(data):
    current_date = data["date_start"]
    date_end = data["date_end"]
    total_stay_length = (date_end - current_date).days

    final_price = 0
    base_day_price = data["property"].base_price / total_stay_length

    while current_date <= date_end:
        # How query works:
        # 1) If min_stay_length is null,
        # specific_day is not null and should be equal to current_date
        # OR
        # 2) If specific_day is null,
        # min_stay_length is not null and should be less than or equal to total_stay_length
        # OR
        # 3) If both specific_day and min_stay_length are not null,
        # both condition must be true

        # How to order by priority:
        # --> first fixed_price (DESC)
        # --> then max min_stay_length (DESC)
        # --> then max price_modifier
        pricing_rule = PricingRule.objects.filter(
            Q(Q(min_stay_length__isnull=True) & Q(specific_day=current_date))
             |
            Q(Q(specific_day__isnull=True) & Q(min_stay_length__lte=total_stay_length))
             |
            Q(Q(specific_day__isnull=False) & Q(min_stay_length__isnull=False) & Q(specific_day=current_date) & Q(min_stay_length__lte=total_stay_length))
            ,
            property_id=data["property"].id
        ).order_by(
            '-fixed_price', '-min_stay_length', 'price_modifier', 
        ).first()

        if pricing_rule is not None:
            if pricing_rule.fixed_price is not None:
                final_price += pricing_rule.fixed_price
            elif pricing_rule.price_modifier is not None:
                final_price += base_day_price * (1 + (pricing_rule.price_modifier / 100.0))
            else:
                final_price += base_day_price
        else:
            final_price += base_day_price
        
        current_date += timedelta(days=1)

    return final_price

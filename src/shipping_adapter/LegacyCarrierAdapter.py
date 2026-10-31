from .shipping_quote_provider import ShippingQuoteProvider
from .legacy_carrier import LegacyCarrier

KG_TO_LB = 2.20462

class LegacyCarrierAdapter(ShippingQuoteProvider):
    def __init__(self, legacy_carrier: LegacyCarrier):
        self.legacyCarrier = legacy_carrier

    def quote(self, destination: str, weight_kg: float) -> float:
        final_weight = weight_kg * KG_TO_LB
        return self.legacyCarrier.get_price(destination, final_weight )
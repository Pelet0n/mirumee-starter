from django.db.models import fields
from django.db.models.lookups import Lookup
from django.db.models import Count
from graphene_django import DjangoObjectType
from graphene.types import field
import graphene
from ...checkout.models import Checkout
from ...checkout.models import CheckoutLine

class CheckoutType(DjangoObjectType):
    total_price = graphene.Decimal(description="Total price of product")

    class Meta:
        model = Checkout
        fields = '__all__'

    def resolve_total_price(self, __info):
        checkout = self.checkout_line.all().product_variant.annotate(total_price=Count('price'))
        total_price = checkout['total_price']
        if not total_price:
            return self.price
        
        return checkout['total_price']

class CheckoutLineType(DjangoObjectType):
    total_price = graphene.Decimal()

    class Meta:
        model = CheckoutLine
        fields = '__all__'

    def resolve_total_price(self, __info):
        checkout_line = self.product_variant.all().annotate(total_price=Count('price'))
        total_price = checkout_line['total_price']
        if not total_price:
            return self.price
        
        return checkout_line['total_price']
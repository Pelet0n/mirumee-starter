from django.db.models import fields
from django.db.models.lookups import Lookup
from django.db.models import Count
from graphene_django import DjangoObjectType
from graphene.types import field
import graphene
from ...checkout.models import Checkout
from ...checkout.models import CheckoutLine

class CheckoutType(DjangoObjectType):
   # total_price = graphene.Decimal(description="Total price of product")

    class Meta:
        model = Checkout
        fields = '__all__'

    """def resolve_total_price(self, __info):
        checkout = self.checkout_line.variants.all().aggregate(total_price=Count('price'))
        total_price = checkout['total_price']
        if not total_price:
            return self.price
        
        return checkout['total_price']
    """
class CheckoutLineType(DjangoObjectType):
    total_price = graphene.Decimal()

    class Meta:
        model = CheckoutLine
        fields = '__all__'

    def resolve_total_price(self, __info):
        total_price = self.objects.all()
        print(total_price)
        return total_price
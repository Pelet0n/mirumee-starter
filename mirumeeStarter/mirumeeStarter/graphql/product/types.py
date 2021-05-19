from graphene.types import field
from graphene_django import DjangoObjectType

from ...product.models import Product, ProductVariant

class ProductType(DjangoObjectType):
    class Meta:
        model = Product
        fields = '__all__'

class ProductVariantType(DjangoObjectType):
    
    class Meta:
        model = ProductVariant
        field = '__all__'
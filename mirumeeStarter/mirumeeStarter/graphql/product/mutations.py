

from django.core.exceptions import ObjectDoesNotExist
import graphene
from graphql_jwt.decorators import staff_member_required
from .types import ProductType, ProductVariantType
from ...product.models import Product, ProductVariant

class ProductCreateInput(graphene.InputObjectType):
    name = graphene.String(required=True)
    price = graphene.Decimal(required=True)
    description = graphene.String(required=True)
    quantity = graphene.Int()

class ProductCreate(graphene.Mutation):
    product = graphene.Field(ProductType)

    class Arguments:
        input = ProductCreateInput(required=True)

    @classmethod
    def clean_price(self, price):
        if int(price) < 0:
            raise Exception("Cena produktu nie może być ujemna!")

    @classmethod
    def clean_input(cls, input):
        cls.clean_price(input['price'])

        return input

    @classmethod
    @staff_member_required
    def mutate(cls, root, info, input):
        cleaned_input = cls.clean_input(input)
        product = Product.objects.create(**cleaned_input)

        return ProductCreate(product=product)

class ProductVariantCreateInput(graphene.InputObjectType):
    name = graphene.String(required=True)
    sku = graphene.String(required=True)
    price = graphene.Decimal()

class ProductVariantCreate(graphene.Mutation):
    product_variant = graphene.Field(ProductVariantType)

    class Arguments:
        input = ProductVariantCreateInput(required=True)
        product_id = graphene.ID(required=True)

    @classmethod
    def clean_price(self, price):
        if int(price) < 0:
            raise Exception("Cena produktu nie może być ujemna!")

    @classmethod
    def clean_sku(self, sku):
        if ProductVariant.objects.filter(sku=sku).exists():
            raise Exception("Wariant produktu z takim sku już istnieje")

    @classmethod
    def clean_productId(self, productId):
        if not ProductVariant.objects.filter(product_id = productId).exists():
            raise Exception("Produkt o podanym id nie istnieje")
            
        

    @classmethod
    def clean_input(cls, input):
        cls.clean_sku(input['sku'])
        cls.clean_price(input['price'])
        #cls.clean_productId(product_id)

        return input

    @classmethod
    @staff_member_required
    def mutate(cls, root, info, input, product_id):
        cleaned_input = cls.clean_input(input)
        product_variant = ProductVariant.objects.create(product_id=product_id, **cleaned_input)

        return ProductVariantCreate(product_variant = product_variant)
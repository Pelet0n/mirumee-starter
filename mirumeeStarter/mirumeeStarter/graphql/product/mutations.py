

import graphene
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
    def clean_input(self, input):
        return input

    @classmethod
    def mutate(self, root, info, input):
        cleaned_input = self.clean_input(input)
        print(cleaned_input)
        product = Product.objects.create(**cleaned_input)

        return ProductCreate(product=product)

class ProductVariantCreateInput(graphene.InputObjectType):
    product_id = graphene.Int(required=True)
    name = graphene.String(required=True)
    sku = graphene.String(required=True)
    price = graphene.Decimal()

class ProductVariantCreate(graphene.Mutation):
    productVariant = graphene.Field(ProductVariantType)

    class Arguments:
        input = ProductVariantCreateInput(required=True)

    @classmethod
    def clean_input(self, input):
        return input

    @classmethod
    def mutate(self, root, info, input):
        cleaned_input = self.clean_input(input)
        productVariant = ProductVariant.objects.create(**cleaned_input)

        return ProductVariantCreate(productVariant = productVariant)
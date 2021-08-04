from itertools import product
import graphene

from .types import ProductType, ProductVariantType
from ...product.models import Product, ProductVariant
from .mutations import ProductCreate, ProductDelete, ProductUpdate, ProductVariantCreate
class ProductQueries(graphene.ObjectType):
    product = graphene.Field(ProductType, id=graphene.Argument(graphene.ID, description="ID of product"))

    products = graphene.List(ProductType)

    productVariant = graphene.Field(ProductVariantType, id=graphene.Argument(graphene.ID, description="ID of product variant"))

    def resolve_product(self, _info, id):
        product = Product.objects.filter(id=id).first()
        return product

        
    def resolve_products(self, _info):
        products = Product.objects.all()
        return products

    def resolve_productVariant(self, _info, id):
        return ProductVariant.objects.filter(id=id).first()

class ProductMutations(graphene.ObjectType):
    product_create = ProductCreate.Field()
    product_variant_create = ProductVariantCreate.Field()
    product_update = ProductUpdate.Field()
    product_delete = ProductDelete.Field()

    
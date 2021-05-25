
import graphene
from .mutations import CheckoutCreate

class CheckoutMutations(graphene.ObjectType):
    checkout_create = CheckoutCreate.Field()

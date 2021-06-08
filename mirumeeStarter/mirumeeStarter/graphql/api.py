import graphene

from ..graphql.product.schema import ProductQueries, ProductMutations
from ..graphql.checkout.schema import CheckoutMutations, CheckoutQueries
from ..graphql.account.schema import UserQueries
from .account.authenticate import AuthenticateMutations
from ..graphql.account.schema import UserMutations

class Query(ProductQueries, UserQueries, CheckoutQueries):
    pass

class Mutations(ProductMutations, CheckoutMutations, AuthenticateMutations, UserMutations):
    pass

schema = graphene.Schema(query=Query, mutation=Mutations)

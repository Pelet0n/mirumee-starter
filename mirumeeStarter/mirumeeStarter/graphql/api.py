import graphene

from ..graphql.product.schema import ProductQueries, ProductMutations
from ..graphql.checkout.schema import CheckoutMutations
from ..graphql.account.authenticate import Mutation


class Query(ProductQueries):
    pass

class Mutations(ProductMutations, CheckoutMutations, Mutation):
    pass

schema = graphene.Schema(query=Query, mutation=Mutations)

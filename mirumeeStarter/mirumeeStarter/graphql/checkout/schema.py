
import graphene
from graphql_jwt.decorators import staff_member_required
from ...checkout.models import Checkout, CheckoutLine
from .mutations import CheckoutCreate, CheckoutLineCreate
from .types import CheckoutLineType, CheckoutType

class CheckoutQueries(graphene.ObjectType):
    checkout = graphene.Field(
        CheckoutType,
        id=graphene.Argument(graphene.ID, description="ID of checkout."),
    )
    checkouts = graphene.List(CheckoutType)
    checkout_line = graphene.Field(
        CheckoutType,
        id=graphene.Argument(graphene.ID, description="Id of checkout line."),
    )
    checkout_lines = graphene.List(CheckoutLineType)

    def resolve_checkout(self, __info, id):
        checkout = Checkout.objects.filter(id=id).first()
        return checkout

    @staff_member_required
    def resolve_checkouts(self, info):
        checkouts = Checkout.objects.all()
        return checkouts

    def resolve_checkout_line(self, info, id):
        checkout_line = CheckoutLine.objects.filter(id=id).first()
        return checkout_line

    def resolve_checkout_lines(self):
        checkout_lines = CheckoutLine.objects.all()
        return checkout_lines

class CheckoutMutations(graphene.ObjectType):
    checkout_create = CheckoutCreate.Field()
    checkout_line_create = CheckoutLineCreate.Field()

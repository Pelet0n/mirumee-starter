

from tabnanny import check
import graphene
from .types import CheckoutType, CheckoutLineType
from ...checkout.models import Checkout, CheckoutLine

class CheckoutLineCreateInput(graphene.InputObjectType):
    variant_id = graphene.ID(required=True)
    quantity = graphene.Int(required=True)

class CheckoutCreateInput(graphene.InputObjectType):
    user_email = graphene.String(required=True)
    user_id = graphene.ID(required=False)
    lines = graphene.List(CheckoutLineCreateInput, required=True)


class CheckoutCreate(graphene.Mutation):
    checkout = graphene.Field(CheckoutType)
    checkout_line = graphene.Field(CheckoutLineType)

    class Arguments:
        input = CheckoutCreateInput(required=True)
        

    @classmethod
    def clean_input(cls, input):
        return input

    @classmethod
    def mutate(cls, root, info, input):
        cleaned_input = cls.clean_input(input)
        lines = cleaned_input.pop('lines')
        
        checkout = Checkout.objects.create(**cleaned_input)
        checkout_lines = []
        for line in lines:
            checkout_lines.append(CheckoutLine(checkout_id=checkout.id, **line))
        checkout_lines.bulk_create(checkout_lines)
        return CheckoutCreate(checkout=checkout)
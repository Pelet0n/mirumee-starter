

from tabnanny import check
import graphene
from django.core.exceptions import ValidationError
from django.core.exceptions import ObjectDoesNotExist
from .types import CheckoutType, CheckoutLineType
from ...checkout.models import Checkout, CheckoutLine
from ...product.models import ProductVariant
from ...account.models import User

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
    def clean_variant_id(cls, variant_id):
        if not ProductVariant.objects.filter(id=variant_id).exists():
            raise Exception("The product variant with the given id does not exist")

    @classmethod
    def clean_quantity(cls, quantity):
        if quantity < 0:
            raise Exception("quantity cannot be less than 0")

    @classmethod
    def clean_user_id(cls, user_id):
        if not User.objects.filter(id=user_id).exists():
            raise Exception("The user with the given id does not exist")

    @classmethod
    def clean_input(cls, input):
        cls.clean_quantity(input['lines'][0].quantity)
        cls.clean_variant_id(input['lines'][0].variant_id)
        cls.clean_user_id(input['user_id'])

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

class CheckoutLineCreate(graphene.Mutation):
    checkout_line = graphene.Field(CheckoutLineType)

    class Arguments:
        input = CheckoutLineCreateInput(required=True)
        checkout_id = graphene.ID(required=True)

    @classmethod
    def clean_variant_id(cls, variant_id):
        if not ProductVariant.objects.filter(id=variant_id).exists():
            raise Exception("The product variant with the given id does not exist")

    @classmethod
    def clean_quantity(cls, quantity):
        if quantity < 0:
            raise Exception("quantity cannot be less than 0")


    @classmethod
    def clean_input(cls, input):
        cls.clean_variant_id(input['variant_id'])
        cls.clean_quantity(input['quantity'])

        return input
    
    @classmethod
    def mutate(cls, root, info, input, checkout_id):
        cleaned_input = cls.clean_input(input)

        variant_id = input.pop('variant_id')
        input_quantity = input.pop('quantity')

        try:
            checkout_line = CheckoutLine.objects.get(checkout_id=checkout_id, variant=variant_id)
        except ObjectDoesNotExist():
            checkout_line = CheckoutLine.objects.create(
                checkout_id=checkout_id,
                variant_id=variant_id,
                quantity=input_quantity)

            return CheckoutLineCreate(checkout_line=checkout_line)

        quantity = checkout_line.quantity + input_quantity

        checkout_line.quantity = quantity
        checkout_line.save()

        return CheckoutLineCreate(checkout_line=checkout_line)
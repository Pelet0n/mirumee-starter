import graphene
from graphql_jwt.decorators import staff_member_required, superuser_required
from .types import UserType
from ...account.models import User
import re


class UserCreateInput(graphene.InputObjectType):
    email = graphene.String(required=True)
    first_name = graphene.String()
    last_name = graphene.String()
    password = graphene.String(required=True)

class UserCreate(graphene.Mutation):
    user = graphene.Field(UserType)

    class Arguments:
        input = UserCreateInput(required=True)

    @classmethod
    def clean_password(cls, password):
        if len(password) < 10:
            raise Exception("password must be at least 10 characters long")
        if not re.search("[A-Z]", password):
            raise Exception("password must be at least 1 uppercase letter")
        if not re.search("[0-9]", password):
            raise Exception("password must be at least 1 number")
        if not re.search("[_@$.*#!()-|\<>%&^]", password):
            raise Exception("password must be at least 1 special character")

    @classmethod
    def clean_email(cls, email):
        if not re.search('^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$', email):
            raise Exception("enter a valid email address")
        if User.objects.filter(email=email).exists():
            raise Exception("This email is already taken")

    @classmethod
    def clean_input(cls, input):
        cls.clean_password(input['password'])
        cls.clean_email(input['email'])

        return input

    @classmethod
    def mutate(cls, root, info, input):
        cleaned_input = cls.clean_input(input)
        user = User.objects.create_user(**cleaned_input)

        return UserCreate(user=user)

class StaffCreate(graphene.Mutation):
    user = graphene.Field(UserType)

    class Arguments:
        input = UserCreateInput(required=True)

    @classmethod
    def clean_password(cls, password):
        if len(password) < 10:
            raise Exception("password must be at least 10 characters long")
        if not re.search("[A-Z]", password):
            raise Exception("password must be at least 1 uppercase letter")
        if not re.search("[0-9]", password):
            raise Exception("password must be at least 1 number")
        if not re.search("[_@$]", password):
            raise Exception("password must be at least 1 special character")

    @classmethod
    def clean_email(cls, email):
        if not re.search('^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$', email):
            raise Exception("enter a valid email address")
        if User.objects.filter(email=email).exists():
            raise Exception("This email is already taken")

    @classmethod
    def clean_input(cls, input):
        cls.clean_password(input['password'])
        cls.clean_email(input['email'])

        return input

    @classmethod
    @superuser_required
    def mutate(cls, root, info, input):
        cleaned_input = cls.clean_input(input)
        user = User.objects.create_user(**cleaned_input, is_staff=True)

        return StaffCreate(user=user)
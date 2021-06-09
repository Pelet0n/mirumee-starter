import graphene
from graphql_jwt.decorators import staff_member_required, superuser_required
from .types import UserType
from ...account.models import User

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
    def mutate(cls, root, info, input):
        user = User.objects.create_user(**input)

        return UserCreate(user=user)

class StaffCreate(graphene.Mutation):
    user = graphene.Field(UserType)

    class Arguments:
        input = UserCreateInput(required=True)

    @classmethod
    @superuser_required
    def mutate(cls, root, info, input):
        user = User.objects.create_user(**input, is_staff=True)

        return StaffCreate(user=user)
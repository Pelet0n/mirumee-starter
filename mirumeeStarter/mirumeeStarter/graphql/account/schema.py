import graphene
from .types import UserType
from graphql_jwt.decorators import staff_member_required
from ...account.models import User
from .mutations import StaffCreate, UserCreate

class UserQueries(graphene.ObjectType):
    user = graphene.Field(UserType, email=graphene.Argument(graphene.String, description = "user email"))

    users = graphene.List(UserType)

    def resolve_user(self, _info, email):
        user = User.objects.filter(email=email).first()
        return user

    @staff_member_required
    def resolve_users(self, _info):
        user = User.objects.all()
        return user

class UserMutations(graphene.ObjectType):
    user_create = UserCreate.Field()
    staff_create = StaffCreate.Field()
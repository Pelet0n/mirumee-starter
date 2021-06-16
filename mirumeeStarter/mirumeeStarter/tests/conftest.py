from decimal import Decimal
from ..product.models import Product
from ..account.models import User
import pytest
from graphene_django.utils.testing import graphql_query
from decimal import Decimal

@pytest.fixture
def client_query(client):
    def func(*args, **kwargs):
        return graphql_query(*args, **kwargs, client=client)
    return func

@pytest.fixture
def products_query():
    products = Product.objects.create(
        name = "Test products",
        description = "Products description",
        price = Decimal("10.00"),
        quantity = 10.00
    )

    return products

@pytest.fixture
def usermutation():
    breakpoint()
    user = User.objects.create(
        email = "test@test.com",
        
        firstName = "test",
        lastName = "test",
        password = "qwerty123456A$"
    )
    
    return user
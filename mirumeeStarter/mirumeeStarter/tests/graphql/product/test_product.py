from ....product.models import Product
import json
from decimal import Decimal

def test_product_by_id(db, client_query):
    product = Product.objects.create(
        name="Test Product",
        description="Product description",
        price=Decimal("-10.00"),
        quantity=10.00
    )

    response = client_query(
        """
        query myproduct($id: ID!) {
            product(id: $id){
                price
                id
                name
                description
                quantity
            }
        }
        """,
        variables={'id':1}
    )
    content = json.loads(response.content)


    product_response = content['data']['product']
    
    assert product_response['id'] == str(product.id)
    assert product_response['description'] == product.description
    assert product_response['quantity'] == product.quantity
    assert product_response['price'] == str(product.price)


def test_products(db, client_query, products_query):
    
    response = client_query(
        """
        query myproducts{
            products{
                id,
                price,
                name,
                description,
                quantity
            }
        }
        """
    )
    content = json.loads(response.content)

    product_response = content['data']['products']
    
    for item in product_response:
        assert item['id'] == str(products_query.id)
        assert item['description'] == products_query.description
        assert item['quantity'] == products_query.quantity
        assert item['price'] == str(products_query.price)
from ....product.models import Product

def test_product_by_id(db, client_query):
    product = Product.objects.create(
        name = "Test Product",
        description = "Product description",
        price = 10,
        quantity = 10
    )

    response = client_query(
        """
        query myproduct($id:ID!){
            product(id: $id){
            price,
            id,
            description,
            quantity
        }
    }
        """,
        op_name='product',
        variables={id:product.id}
    )

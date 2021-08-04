import React from 'react'
import {gql} from 'apollo-boost'
import {useMutation, useQuery} from 'react-apollo'
import { DeleteProduct } from './Delete';

const QUERY_PRODUCTS = gql`
query{
    products{
      name,
      id,
      description,
      quantity,
      price
    }
  }
`;

const ADD_PRODUCT = gql`
mutation add_product($name: String!,$price: Decimal!, $description: String!, $quantity: Int ){
    productCreate(input:{name:$name, price:$price, description:$description, quantity:$quantity}){
      product{
        id,
        name,
        price,
        description,
          quantity
      }
    }
  }
`

export function ProductInfo(){
    const {data, loading, error} = useQuery(
        QUERY_PRODUCTS,
        {
            pollInterval: 5000
        }
    );
    

    if (loading){
       return <p>Loading....</p>
    };

    if (error){
        return <p>Error {error.message}</p>
    }

    
    return data.products.map(({name, id, quantity, description, price}) => (
        <div key={id} class="mb-4">
            <p>Product - {id} <br/> name: {name} <br/> price: {price} <br/> description: {description} <br/> quantity: {quantity}</p>
            <DeleteProduct product_id={id}/>
        </div>
    ));
}

export function AddProduct(){
    let name, price, description, quantity;
    const [addProduct,{data, loading, error}] = useMutation(ADD_PRODUCT)

    if (loading) return <p>Submitting data...</p>
    if (error) return alert("Error: " + error.message)


    return(
        <div>
            <form onSubmit={e => {
                e.preventDefault()
                if(name.value === '' || price.value === '' || description.value === ''){
                    return alert('Pola muszą być zapełnione!')
                }
                if (quantity.value !== ''){
                    addProduct({variables: {name: name.value, price: price.value, description: description.value, quantity: parseInt(quantity.value)}})
                }
                else{
                    addProduct({variables: {name: name.value, price: price.value, description: description.value}})
                }
            

                name.value = ''
                price.value = ''
                description.value = ''
                quantity.value = ''
            }}>
                <div class="row mt-5">
                    <div class="col-md-4 form-floating">
                        <input class="form-control" type="text" placeholder="name" ref={node => {
                            name = node;
                        }}/>
                        <label>Name</label>
                    </div>
                
                    <div class="col-md-2 form-floating">
                        <input class="form-control" placeholder="Price" type="Number" ref={node => {
                            price = node;
                        }}/>
                        <label>Price</label>
                    </div>
                </div>
                <div class="row mb-5 mt-2">
                    <div class="col-md-4 form-floating">
                        <textarea style={{height: '150px', resize:'none'}} placeholder="Description" class="form-control" ref={node => {
                            description = node;
                        }}/>
                        <label>Description</label>
                    </div>
                    
                    <div class="col-md-2 form-floating">
                        <input class="form-control" placeholder="Quantity(optional)" type="Number" ref={node => {
                            quantity = node;
                        }}/>
                        <label>Quantity(optional)</label>
                    </div>
                </div>
                    <button type="submit" class="btn btn-success" style={{cursor: 'pointer'}}>Add product</button>
                
            </form>
        </div>
    )
}
    
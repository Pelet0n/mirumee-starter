import React from 'react'
import {gql} from 'apollo-boost'
import { useMutation } from 'react-apollo'

const DELETE_PRODUCT = gql`
mutation deleteProduct($product_id:ID!){
    productDelete(productId: $product_id){
      product{
        id
      }
    }
  }
`


export function DeleteProduct({product_id}){
    
    const [deleteProduct, {data, loading, error}] = useMutation(DELETE_PRODUCT)

    if (loading){
        return <p>Deleting...</p>
    }
    if(error){
        return <p style={{color:'red'}}>Error {error.message}</p>
    }

    return(
      <div>
        <button class="btn btn-danger" data-bs-toggle="modal" data-bs-target="#deleting">Delete product</button>

        <div class="modal fade" id="deleting" tabIndex="-1" aria-labelledby="deletingLabel" aria-hidden="true">
          <div class="modal-dialog">
            <div class="modal-content">
                <div class="modal-header">
                  <h3 class="modal-title">Are you sure?</h3>
                  <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                  <p>This procedure will remove the product from the store</p>
                </div>
                <div class="modal-footer">
                  <button class="btn btn-primary" data-bs-dismiss="modal">Close</button>
                  <button class="btn btn-danger" data-bs-dismiss="modal" onClick={e =>{
                    e.preventDefault()
                    console.log(product_id)
                    deleteProduct({variables: {product_id: product_id}})         
                  }
                  }>Delete product</button>
                  
                </div>
            </div>
          </div>
        </div>
      </div>
        
    )

}
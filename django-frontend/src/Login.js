import React from 'react'
import {gql} from 'apollo-boost'
import { useMutation } from 'react-apollo'

const AUTH_USER = gql`
mutation auth_user($email: String!, $password: String!){
    tokenAuth(email: $email, password: $password){
      token
    }
  }
`


export function Login(){
    let email, password
    const [authUser, {data, loading, error}] = useMutation(AUTH_USER)

    if (loading){
        return <p>Login in...</p>
    }
    if (error){
        return <p>Error {error.message}</p>
    }

    return (
        
        <div>
            <form onSubmit={e =>{
                e.preventDefault()
                authUser({variables: {email: email.value, password: password.value}})
                console.log(data)
                email.value = ''
                password.value = ''
                
            }}>
                <input type="email" placeholder="email" class="form-control" ref={node =>{
                    email = node
                }}/>
                <input type="password" placeholder="password" class="form-control" ref={node =>{
                    password = node
                }}/>
                <button type="submit" class="btn btn-success">Login</button>
            </form>
        </div>
    )
}
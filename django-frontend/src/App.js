import React from 'react'
import ApolloClient from 'apollo-boost'
import {ApolloProvider} from 'react-apollo'
import { AddProduct, ProductInfo } from './Product';
import {BrowserRouter, Route, Switch, Redirect} from 'react-router-dom'
import { Login } from './Login';

const client = new ApolloClient({
  uri: 'http://localhost:8000/graphql/'
}
);

function App() {
  return (
    <ApolloProvider client={client}>
       
      
      <BrowserRouter>
        <Switch>
          <Route path="/produkty">
            <h1>My first Apollo aplication</h1>

            <ProductInfo/>
            <AddProduct/>
          </Route>
          <Route path="/login">
            <Login/>
          </Route>
          <Route path="/">
            <Redirect to="/produkty"></Redirect>
          </Route>
        </Switch>
      </BrowserRouter>
    </ApolloProvider>
  );
    
}

export default App;

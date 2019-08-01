import React from "react"
import { render } from "react-dom"
import ApolloClient from "apollo-boost"
import { ApolloProvider } from "@apollo/react-hooks"
import { App } from "./app"


const client = new ApolloClient({
    uri: "http://localhost:5000/graphql",
})

const Root = () => (
    <ApolloProvider client={client}>
      <App/>
    </ApolloProvider>
)

render(<Root/>, document.getElementById("root"))


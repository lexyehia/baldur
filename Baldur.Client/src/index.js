import React from "react"
import { render } from "react-dom"
import ApolloClient from "apollo-boost"
import { ApolloProvider } from "@apollo/react-hooks"
import { Base } from "./base"


const client = new ApolloClient({
    uri: "http://localhost:5000/graphql",
})

const Root = () => (
    <ApolloProvider client={client}>
      <Base anyProp/>
    </ApolloProvider>
)

render(<Root/>, document.getElementById("root"))

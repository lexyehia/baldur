import "./main.scss"

import React from "react"
import {render} from "react-dom"
import {ApolloProvider} from "@apollo/react-hooks"
import ApolloClient from "apollo-boost"
import {Base} from "./components/Base"


const client = new ApolloClient({
    uri: 'http://localhost:5000/graphql'
})

render(
    <ApolloProvider client={client}>
        <Base/>
    </ApolloProvider>,
    document.getElementById("app")
)

import React from "react"
import "./main.scss"
import {render} from "react-dom"
import {ApolloProvider} from "@apollo/react-hooks"
import {client} from "./shared/apollo";
import {Base} from "./components/Base"

render(
    <ApolloProvider client={client}>
        <Base/>
    </ApolloProvider>,
    document.getElementById("app")
)

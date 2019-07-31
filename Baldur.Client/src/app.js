import React from "react";
import { getUser } from "./queries/test.gql";
import { print } from "graphql/language/printer";

export default class HelloComponent extends React.Component {
    constructor(props) {
        super(props);

        this.state = {
            item: null,
        };
    }

    componentDidMount() {
        runQuery(getUser);
    }

    render() {
        return <div>Hello there {this.state.item}</div>;
    }

}

export function runQuery(query, variables = {}) {
    if (typeof query === "object") {
        query = print(query)
    }

    fetch("http://localhost:5000/graphql", {
        method: "POST",
        headers: {
            "content-type": "application/json",
            "Accept": "application/json",
        },
        body: JSON.stringify({ query, variables })
    });
}


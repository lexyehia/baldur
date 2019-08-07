import React, { useState } from "react"
import PropTypes from "prop-types"
import { useQuery } from "@apollo/react-hooks"
import { GET_USER } from "./queries/test.graphql"
import gql from "graphql-tag";

export const App = () => {
    const [item, setItem] = useState(null)
    const { loading, data } = useQuery(GET_USER)

    if (!loading && item === null) {
        setItem(data)
    }

    if (item) {
        return <div>{item.user.email}</div>
    } else {
        return <div>Loading...</div>
    }
};

const fragment = gql`
    mutation ($password: String) {
        createUser(email: $password) {
            id
        }
    }
`;

App.propTypes = {
    anyProp: PropTypes.bool.isRequired,
};

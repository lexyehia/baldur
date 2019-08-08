import React from "react"
import PropTypes from "prop-types"
import { useQuery } from "@apollo/react-hooks"
import gql from "graphql-tag";
import styled from "styled-components"

const Wrapper = styled.div`
  color: red;
  font-family: 'Consolas', 'Deja Vu Sans Mono', 'Bitstream Vera Sans Mono', monospace;
  
  p {
    color: antiquewhite;
  }
`

export const Base = ({ anyProp }) => {
    const { loading, data } = useQuery(query)

    if (anyProp) {
        return null
    }

    if (!loading && data) {
        return (
            <Wrapper>
                <p>{data.users[0].id}</p>
            </Wrapper>
        )
    } else {
        return <Wrapper><p>Loading...</p></Wrapper>
    }
};

const query = gql`
    query {
        users {
            id
        }
    }
`

Base.propTypes = {
    anyProp: PropTypes.bool.isRequired,
};

import React from "react"
import styled from "styled-components"
import PropTypes from "prop-types"
import {useState} from "react";
import gql from "graphql-tag"

const Wrapper = styled.div`
  color: red;
  font-family: 'Consolas', 'Deja Vu Sans Mono', 'Bitstream Vera Sans Mono', monospace;
  
  p {
    color: rebeccapurple;
  }
`

const query = gql`
    query {
        users {
            email,
        }
    }
`

export const Base = (props) => {
    const [person, setPerson] = useState({ name: 'Hello' })

    return (
        <Wrapper className='test'>
            <p onClick={() => setPerson({ name: 'Bob' })}>Hello World {person.name}</p>
        </Wrapper>
    )
}

Base.propTypes = {
}

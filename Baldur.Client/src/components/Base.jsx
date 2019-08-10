import React from "react"
import styled from "styled-components"
import PropTypes from "prop-types"
import {useState} from "react";
import gql from "graphql-tag"
import {useRouter} from "../shared/router";
import {RegisterView} from "../views/Register/RegisterView";
import {LoginView} from "../views/Login/LoginView";

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

const routes = [
    { path: '/register/:person?', component: ({ person }) => <RegisterView person={person} /> },
    { path: '/login/(.*)', component: () => <LoginView/> }
]

export const Base = (props) => {
    const component = useRouter(routes)

    return (
        <Wrapper className='test'>
            {component}
        </Wrapper>
    )
}

Base.propTypes = {
}

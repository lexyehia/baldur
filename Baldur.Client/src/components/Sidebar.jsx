import React from "react"
import PropTypes from "prop-types"
import styled from "styled-components"
import {Wrapper} from "./Wrapper";


export const Sidebar = () => {
    return (
        <Container>
            Item 1
        </Container>
    )
}

const Container = styled(Wrapper)`
  height: 100%;
  width: 160px;
  position: fixed;
  z-index: 9;
  top: 0;
  left: 0;
  background-color: #92d4af;
  color: black;
  overflow-x: hidden;
  padding-top: 80px;
`

Sidebar.propTypes = {}

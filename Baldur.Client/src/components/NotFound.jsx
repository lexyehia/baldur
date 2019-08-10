import React from "react"
import PropTypes from "prop-types"
import styled from "styled-components"


export const NotFound = () => {
    return (
        <Container>
            Not Found
        </Container>
    )
}

const Container = styled.div`
  color: red;
`

NotFound.propTypes = {
}

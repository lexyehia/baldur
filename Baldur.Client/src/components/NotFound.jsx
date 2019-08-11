import React from "react"
import PropTypes from "prop-types"
import styled from "styled-components"
import { MainContent } from "shared/stylistics"


export const NotFound = () => {
    return (
        <Container>
            Not Found
        </Container>
    )
}

const Container = styled(MainContent)`
  color: red;
`

NotFound.propTypes = {
}

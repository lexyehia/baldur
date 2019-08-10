import React from "react"
import PropTypes from "prop-types"

export const RegisterView = (props) => {
    return (
        <div>
            Register {props.person}
        </div>
    )
}

RegisterView.propTypes = {
    person: PropTypes.string
}
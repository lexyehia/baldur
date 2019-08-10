import React, {useCallback} from "react"
import PropTypes from "prop-types"

export const Link = ({ to, children }) => {
    const onClick = useCallback(() => {
        window.location = to
    }, [to])

    return (
        <a href="#" onClick={onClick}>
            {children}
        </a>
    )
}

Link.propTypes = {
    to: PropTypes.string.isRequired,
    children: PropTypes.element,
}
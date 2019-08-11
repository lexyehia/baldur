import React, {useCallback} from "react"
import PropTypes from "prop-types"

export const Link = ({ to, className, children }) => {
    const onClick = useCallback((e) => {
        e.preventDefault()
        window.location.href = to
    }, [to])

    return (
        <a className={className} href="#" onClick={onClick}>
            {children}
        </a>
    )
}

Link.propTypes = {
    to: PropTypes.string.isRequired,
    className: PropTypes.string,
    children: PropTypes.any
}

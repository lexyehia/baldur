import React, {useCallback} from "react";

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
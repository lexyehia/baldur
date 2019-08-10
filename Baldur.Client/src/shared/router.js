import React from "react";
import pathToRegexp from "path-to-regexp"

export function useRouter(routes) {
    if (!Array.isArray(routes)) {
        throw new Error("routes arg is not an array")
    }

    const path = window.location.pathname
    let component = null

    for (const route of routes) {
        const keys = []
        const pathRegex = pathToRegexp(route.path, keys)

        if (pathRegex.test(path)) {
            const props = {}

            if (keys.length > 0) {
                const values = pathRegex.exec(path).slice(1)
                keys.forEach((key, i) => {
                    props[key.name] = values[i]
                })
            }

            component = route.component(props)
            break
        }
    }
    
    return component
}
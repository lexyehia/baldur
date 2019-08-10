import React from "react";
import pathToRegexp from "path-to-regexp"

export function useRouter(routes) {
    if (typeof routes !== "object") {
        throw new Error("routes arg is not an array")
    }

    const path = window.location.pathname
    let component = null

    for (const routePath in routes) {
        if (!{}.hasOwnProperty.call(routes, routePath)) continue

        const keys = []
        const pathRegex = pathToRegexp(routePath, keys)

        if (pathRegex.test(path)) {
            const props = {}

            if (keys.length > 0) {
                const values = pathRegex.exec(path).slice(1)
                keys.forEach((key, i) => {
                    props[key.name] = values[i]
                })
            }

            component = routes[routePath](props)
            break
        }
    }
    
    return component
}
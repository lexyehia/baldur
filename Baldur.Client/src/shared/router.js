import pathToRegexp from "path-to-regexp"


export function useRouter(routes) {
    if (typeof routes !== "object") {
        throw new Error("routes arg is not an array")
    }

    const path = window.location.pathname
    let component = null

    for (const routePath in routes) {
        if (!{}.hasOwnProperty.call(routes, routePath)) continue
        if (typeof routePath !== "string" || typeof routes[routePath] !== "function") continue

        const keys = []
        const routeRegex = pathToRegexp(routePath, keys)

        if (routeRegex.test(path)) {
            const props = {}

            if (keys.length > 0) {
                const values = routeRegex.exec(path).slice(1)
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
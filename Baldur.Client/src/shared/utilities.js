/**
 * Returns a string with first letter upper-cased
 * @param {string} str
 * @returns {string|*}
 */
export function toUpperFirstLetter(str) {
    if (typeof str !== "string") return str
    return str.charAt(0).toUpperCase() + str.slice(1)
}

/**
 * Returns a string with first letter upper-cased
 * @param {string} str
 * @returns {string|*}
 */
export function toUpperFirstLetter(str) {
    if (typeof str !== "string") return str
    return str.charAt(0).toUpperCase() + str.slice(1)
}

/**
 * Convert a
 * @param amount
 * @param currency
 * @returns {string}
 */
export function toCurrency(amount, currency = "CAD") {
    const formatter = new Intl.NumberFormat("en-CA", { style: "currency", currency })
    return formatter.format((amount / 100).toFixed(2))
}

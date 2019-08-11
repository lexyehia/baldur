import { gql } from "apollo-boost"

export const ADD_TRANSACTION = gql`
    mutation ($amount: Int) {
        addTransaction(amount: $amount, date: ${Number(Date.now())}, description: "Hello") {
            id,
            sum,
        }
    }
`


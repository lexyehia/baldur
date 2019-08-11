import React, { useCallback, useState } from "react"
import PropTypes from "prop-types"
import styled from "styled-components"
import { COLORS } from "shared/stylistics"
import { useMutation } from "@apollo/react-hooks"
import { ADD_TRANSACTION } from "../../graphql/mutations"

export const TransactionForm = () => {
    const [amount, setAmount] = useState(0)
    const [addTaskAsync] = useMutation(ADD_TRANSACTION)

    const submitForm = useCallback((e) => {
        e.preventDefault()

        const payload = {
            amount: Number(amount),
            date: Date.now(),
            description: "Random transaction",
        }

        console.log(payload)
        addTaskAsync({ variables: {
            amount: amount,
        }})
    }, [addTaskAsync, amount])

    return (
        <Container>
            <div className="form-group">
                <label>
                    Amount
                </label>
                <input
                    type="text"
                    className="form-control"
                    placeholder="Transaction amount"
                    value={amount}
                    onChange={e => setAmount(e.target.value)}
                />
            </div>
            <button
                type="submit"
                className="btn btn-primary"
                onClick={submitForm}
            >
                Add
            </button>
        </Container>
    )
}

const Container = styled.div`
  color: ${COLORS.DarkGrey};
`

TransactionForm.propTypes = {}

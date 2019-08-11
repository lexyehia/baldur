import React from "react"
import PropTypes from "prop-types"
import styled from "styled-components"
import { DataTable } from "components/DataTable";
import { Sidebar } from "components/Sidebar";
import { MainContent } from "shared/stylistics";
import { toCurrency } from "shared/utilities"
import { TransactionForm } from "views/LedgerView/TransactionForm"

const fakeData = [
    { account: "Bank", amount: toCurrency(1003432), date: Date.now() },
    { account: "Expense", amount: toCurrency(200), date: Date.now() }
]

export const LedgerView = () => {
    return (
        <Container>
            <Sidebar/>
            <MainContent>
                <DataTable data={fakeData} />
                <TransactionForm/>
            </MainContent>
        </Container>
    )
}

const Container = styled.div`
  color: red;
`

LedgerView.propTypes = {}

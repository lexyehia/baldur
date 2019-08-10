import React from "react"
import PropTypes from "prop-types"
import styled from "styled-components"
import {DataTable} from "../../components/DataTable";
import {Sidebar} from "../../components/Sidebar";
import {MainContent} from "../../components/Wrapper";

const fakeData = [
    { account: "Bank", amount: 1000, date: Date.now() },
    { account: "Expense", amount: 200, date: Date.now() }
]

export const LedgerView = () => {
    return (
        <Container>
            <Sidebar/>
            <MainContent>
                <DataTable data={fakeData} />
            </MainContent>
        </Container>
    )
}

const Container = styled.div`
  color: red;
`

LedgerView.propTypes = {}

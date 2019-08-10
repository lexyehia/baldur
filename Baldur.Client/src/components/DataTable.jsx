import React from "react"
import PropTypes from "prop-types"
import styled from "styled-components"

const DataRow = ({ data }) => {
    const cells = Object.keys(data).map(k => (
        <div key={k}>{data[k]}</div>
    ))

    return (
        <div>
            {cells}
        </div>
    )
}

DataRow.propTypes = {
    columns: PropTypes.instanceOf(Set).isRequired,
    data: PropTypes.object.isRequired,
}

export const DataTable = ({ data }) => {
    const columns = data.reduce((acc, row) => {
        Object.keys(row).forEach(acc.add)
        return acc
    }, new Set())

    const headers = Array.from(columns).map(c => (
        <div key={c}>{c}</div>
    ))

    const rows = data.map((d, i) => (
        <DataRow key={i} data={d} columns={columns}/>
    ))

    return (
        <Container>
            <div>
                {headers}
            </div>
            {rows}
        </Container>
    )
}

const Container = styled.div`
  color: red;
`

DataTable.propTypes = {
    data: PropTypes.arrayOf(PropTypes.object).isRequired,
}

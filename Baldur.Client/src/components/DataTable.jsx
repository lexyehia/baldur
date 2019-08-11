import React from "react"
import PropTypes from "prop-types"
import styled from "styled-components"
import { COLORS } from "shared/stylistics"
import { toUpperFirstLetter } from "shared/utilities"

/**
 * A basic data row component
 * @param {Object} data
 * @returns {React.ReactElement}
 */
const DataRow = ({ data }) => {
    const cells = Object.keys(data).map(k => (
        <TableCell key={k}>{data[k]}</TableCell>
    ))

    return (
        <TableRow>
            {cells}
        </TableRow>
    )
}

DataRow.propTypes = {
    columns: PropTypes.instanceOf(Set).isRequired,
    data: PropTypes.object.isRequired,
}

const TableRow = styled.div`
  display: table-row;
  width: auto;
  clear: both;
`

const TableCell = styled.div`
  float: left;
  display: table-column;
  width: 200px;
  background-color: ${COLORS.Grey};
  color: black;
  padding: 3px;
`

/**
 * A Data Table Component
 * @param {Object} data
 * @returns {React.ReactElement}
 */
export const DataTable = ({ data }) => {
    const columns = data.reduce((acc, row) => {
        Object.keys(row).forEach(k => {
            acc.add(k)
        })
        return acc
    }, new Set())

    const headers = Array.from(columns).map(c => (
        <TableHeader key={c}>{toUpperFirstLetter(c)}</TableHeader>
    ))

    const rows = data.map((d, i) => (
        <DataRow key={i} data={d} columns={columns}/>
    ))

    return (
        <Container>
            <TableRow>
                {headers}
            </TableRow>
            {rows}
        </Container>
    )
}

DataTable.propTypes = {
    data: PropTypes.arrayOf(PropTypes.object).isRequired,
}

const Container = styled.div`
  display: table;
  width: auto;
  background-color: ${COLORS.Grey};
  border: 2px solid #666666;
`

const TableHeader = styled(TableCell)`
  background-color: ${COLORS.DarkGrey};
  font-weight: bold;
  color: white;
  border-bottom: 2px solid ${COLORS.DarkGrey};
`

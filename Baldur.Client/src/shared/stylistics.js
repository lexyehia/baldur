import styled from "styled-components"

/**
 * Primary Colours used throughout the App
 */
export const COLORS = {
    Green: "rgba(32, 191, 107,1.0)",
    Red: "rgba(235, 59, 90,1.0)",
    Mauve: "rgba(136, 84, 208,1.0)",
    DarkGrey: "rgba(75, 101, 132,1.0)",
    Grey: "rgba(165, 177, 194,1.0)",
    Silver: "rgba(209, 216, 224,1.0)",
}

export const Wrapper = styled.div`
  color: black;
  background-color: white;
`

export const MainContent = styled(Wrapper)`
  padding-left: 170px;
  padding-top: 10px;
`

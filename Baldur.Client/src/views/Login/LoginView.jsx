import React from "react"
import styled from "styled-components"
import {Sidebar} from "../../components/Sidebar";
import {Wrapper} from "../../components/Wrapper";

export const LoginView = (props) => {
    return (
        <div>
            <Sidebar/>
            <ContentBox>
                Login
            </ContentBox>
        </div>
    )
}

const ContentBox = styled(Wrapper)`
  padding-left: 160px;
`

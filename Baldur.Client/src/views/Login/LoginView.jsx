import React from "react"
import styled from "styled-components"
import {Sidebar} from "../../components/Sidebar";
import {MainContent} from "../../components/Wrapper";

export const LoginView = (props) => {
    return (
        <div>
            <Sidebar/>
            <MainContent>
                Login
            </MainContent>
        </div>
    )
}

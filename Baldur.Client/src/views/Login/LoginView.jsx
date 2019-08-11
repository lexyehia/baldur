import React from "react"
import styled from "styled-components"
import {Sidebar} from "../../components/Sidebar";
import {MainContent} from "../../shared/stylistics";

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

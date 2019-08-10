import React from "react"
import styled from "styled-components"
import {useRouter} from "../shared/router";
import {RegisterView} from "../views/Register/RegisterView";
import {LoginView} from "../views/Login/LoginView";
import {Menu} from "./Menu";
import {NotFound} from "./NotFound";


const routes = {
    "/register": (props) => <RegisterView {...props} />,
    "/login": () => <LoginView/>
}

export const Base = () => {
    const route = useRouter(routes)

    return (
        <Container>
            <Menu/>
            <div id="content">
                {route || <NotFound/>}
            </div>
        </Container>
    )
}

const Container = styled.div`
  width: 100%;
  height: 100%;
  
  div#content {
    padding-top: 75px;
  }
`

Base.propTypes = {
}

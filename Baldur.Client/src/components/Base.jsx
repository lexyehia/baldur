import React from "react"
import styled from "styled-components"
import {useRouter} from "../shared/router";
import {RegisterView} from "../views/Register/RegisterView";
import {LoginView} from "../views/Login/LoginView";
import {Menu} from "./Menu";


const routes = {
    '/register/:person?': (props) => <RegisterView {...props} />,
    '/login/(.*)': () => <LoginView/>
}

export const Base = () => {
    const component = useRouter(routes)

    return (
        <Container>
            <Menu/>
            <div className="Menu">hello</div>
        </Container>
    )
}

const Container = styled.div`
  width: 100%;
  height: 100%;
`

Base.propTypes = {
}

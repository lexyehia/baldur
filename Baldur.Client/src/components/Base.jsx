import React from "react"
import styled from "styled-components"
import {useRouter} from "../shared/router";
import {RegisterView} from "../views/Register/RegisterView";
import {LoginView} from "../views/Login/LoginView";


const routes = {
    '/register/:person?': (props) => <RegisterView {...props} />,
    '/login/(.*)': () => <LoginView/>
}

export const Base = () => {
    const component = useRouter(routes)

    return (
        <Container>
            <div className="Side">hi<br/>There</div>
            <div className="Menu">hello</div>
        </Container>
    )
}

const Container = styled.div`
  display: grid;
  grid-template-columns: 0.6fr 1.4fr 1fr 1fr;
  grid-template-rows: 0.3fr 1.7fr 1fr;
  grid-template-areas: "Side Menu Menu Menu" "Side . . ." "Side . . .";

  .Side { grid-area: Side; background-color: black; }  
  .Menu { grid-area: Menu; }
`

const Wrapper = styled.div`
  color: red;
  font-family: 'Consolas', 'Deja Vu Sans Mono', 'Bitstream Vera Sans Mono', monospace;
  
  p {
    color: rebeccapurple;
  }
`

Base.propTypes = {
}

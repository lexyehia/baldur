import React from "react"
import styled from "styled-components"
import {Wrapper} from "./Wrapper";

export const Menu = () => {
    return (
        <Container className="navbar navbar-expand-lg">
            <a className="navbar-brand" href="#">Brand</a>
            <div className="collapse navbar-collapse">
                <div className="navbar-nav">
                    <a className="nav-item nav-link" href="#">Home</a>
                    <a className="nav-item nav-link" href="#">Reports</a>
                    <a className="nav-item nav-link" href="#">Charts</a>
                </div>
            </div>
        </Container>
    )
}

const Container = styled(Wrapper)`
    position: absolute;
    background-color: black;
    margin-bottom: 10px;
    color: white;
    width: 100%;
    height: 75px;
    z-index: 10;
    
    .navbar-brand {
      color: white;
    }
    
    .nav-link {
      color: white;
      
      &:hover {
        color: antiquewhite;
      }
    }
`

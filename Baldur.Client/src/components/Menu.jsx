import React from "react"
import styled from "styled-components"

export const Menu = (props) => {
    return (
        <Container className="navbar navbar-expand-lg">
            <a href="#" className="navbar-brand">Brand</a>
            <div className="collapse navbar-collapse">
                <div className="navbar-nav">
                    <a className="nav-item nav-link" href="#">Reports</a>
                    <a className="nav-item nav-link" href="#">Reports</a>
                    <a className="nav-item nav-link" href="#">Reports</a>
                </div>
            </div>
        </Container>
    )
}

const Container = styled.nav`
    position: absolute;
    background-color: black;
    margin-bottom: 10px;
    color: white;
    width: 100%;
    height: 75px;
    
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
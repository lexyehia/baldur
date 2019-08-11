import React from "react"
import styled from "styled-components"
import { Wrapper, COLORS } from "../shared/stylistics";
import { Link } from "components/Link"


export const Menu = () => {
    return (
        <Container className="navbar navbar-expand-lg">
            <a className="navbar-brand" href="#">Brand</a>
            <div className="collapse navbar-collapse">
                <div className="navbar-nav">
                    <Link to="/" className="nav-item nav-link">Home</Link>
                    <Link to="/reports" className="nav-item nav-link">Reports</Link>
                    <Link to="/charts" className="nav-item nav-link">Charts</Link>
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
        color: ${COLORS.Silver};
      }
    }
`

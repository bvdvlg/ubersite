import classes from "./Header.module.css"
import tools from "./tools.svg"
import { NavLink } from "react-router-dom";
import InstrumentsMenu, { Menu } from "./InstrumentsMenu"
import { useState } from "react";

function NavItem({children, path, onClick}) {
    if (path) {
        return (
            <NavLink className={classes.navItemContainer} to={path} >
                        <div className={classes.navLink} >{children}</div>
            </NavLink>
        )
    } else if (onClick) {
        return (
            <div onClick={onClick} className={classes.navItemContainer} >
                <div className={classes.navLink} >{children}</div>
            </div>);
    } else {
        return (
            <div className={classes.navItemContainer} >
                <div className={classes.navLink} >{children}</div>
            </div>);
    }
}

export default function Navbar (props) {
    const [funcMenu, setFuncMenu] = useState(false);
    function onClick () {
        setFuncMenu(true)
    }

    return (
        <>
            <NavItem path="/" >Home</NavItem>
            <NavItem onClick={onClick} >
                <div >Instruments <img src={tools} /></div>
            </NavItem>
            <NavItem path="/about" >About</NavItem>
            <InstrumentsMenu open={funcMenu} onClick={() => {setFuncMenu(false)}} >
                    <Menu />
            </InstrumentsMenu>
        </>
    )
}
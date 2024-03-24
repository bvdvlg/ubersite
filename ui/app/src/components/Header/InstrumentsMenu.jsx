import { useRef } from "react"
import { useEffect } from "react"
import { createPortal } from "react-dom"
import classes from "./Header.module.css"
import logo from "./tools_black.svg"

import { Link, NavLink } from "react-router-dom"

function ToolItem ({children, image, path}) {
    return (
        <>
            <NavLink to={path} >
                <div className={classes.toolsItem}>
                    <img src={image} className={classes.itemImage} ></img>
                    <div className={classes.itemText} style={{textDecoration: "none"}} >{children}</div>
                </div>
            </NavLink>
        </>
    )
}

export function Menu (props) {
    return (
        <div className={classes.toolsContainer}>
            <ToolItem image={logo} path="/tools/replacer" >Text Replacer</ToolItem>
            <ToolItem image={logo} path="/tools/json2dict" >Json to Dict</ToolItem>
            <ToolItem image={logo} path="/tools/code_executor" >Code Executor</ToolItem>
        </div>
    )
}

export default function InstrumentsMenu ({ children, open, onClick }) {
    const dialog = useRef()

    useEffect(() => {
        if (open) {
            console.log("Showing modal")
            dialog.current.showModal()
        } else {
            dialog.current.close()
        }
    }, [open])

    return createPortal(
        <dialog onClick={onClick} ref={dialog} >{children}</dialog>, document.getElementById("modal")
    )
}
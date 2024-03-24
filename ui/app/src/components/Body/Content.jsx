import { Routes, Route } from "react-router-dom";
import ToolsBodyRouter from "./ToolsBodyRouter";
import About from "./About";
import classes from "./Body.module.css"
import gosling from "./gosling.jpeg"

export default function Content (props) {
    return (
        <div id={classes.commonContent} >
            <Routes>
                <Route exact path="/" element={(<img src={gosling} />)} />
                <Route exact path="/about" element={(<About />)} />
                <Route exact path="/tools/*" element={(<ToolsBodyRouter />)} />
            </Routes>
        </ div>
    )
}
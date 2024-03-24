import classes from "./Json2Dict.module.css"
import { useState } from "react";

export default function Json2Dict (props) {
    const [input, setInput] = useState("");
    const [output, setOutput] = useState("")

    return (
        <div className={classes.mainContainer}>
            <div className={classes.inputTextField}>
                <label htmlFor="input" >Text to replace here</label>
                {<textarea style={{height: "100%", resize: "none"}} placeholder="Text value" onChange={(event) => {console.log(event.target.value);setInput(event.target.value)}} id="input" type="text" ></textarea>}
            </div>
            <div className={classes.outputTextField}>
                <label htmlFor="output" >Replaced text here</label>
                {<textarea style={{height: "100%", resize: "none"}} placeholder="Text value" value={output} id="output" type="text" readOnly={true} ></textarea>}
            </div>
        </div>
    )
}
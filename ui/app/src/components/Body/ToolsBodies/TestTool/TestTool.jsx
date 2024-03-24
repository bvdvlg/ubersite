import classes from "./TestTool.module.css"
import { useState, useEffect, useCallback, useRef } from "react";
import axios from "axios"

export default function TestTool (props) {
    const [input, setInput] = useState("");
    const [toSearch, setToSearch] = useState("")
    const [toReplace, setToReplace] = useState("")
    const [output, setOutput] = useState("")
    const cooldownActive = useRef(false);
    const needUpdateAfterCooldown = useRef(false);
    const [inputRef, toSearchRef, toReplaceRef] = [useRef(), useRef(), useRef()]
    

    useEffect(() => {
        function updateOutput() {
            axios.post("http://158.160.22.115:8000/replace", {
                    "data": inputRef.current.value,
                    "filter_regexp": toSearchRef.current.value,
                    "replace_text": toReplaceRef.current.value
                }, {
                headers: {
                    "Content-Type": "application/json"
            }}).then((data) => {setOutput(data.data.body ? data.data.body : "");}).catch((error) => {console.log("here is an error", error)})
        }

        if (input && toSearch && toReplace && !cooldownActive.current) {
            updateOutput()
            cooldownActive.current = true;
            setTimeout(() => {
                cooldownActive.current = false;
                if (needUpdateAfterCooldown.current) {
                    updateOutput()
                }
                needUpdateAfterCooldown.current = false
            }, 2000)
        } else if (cooldownActive) {
            needUpdateAfterCooldown.current = true
        } else {
            setOutput("")
        }
    }, [input, toSearch, toReplace, cooldownActive, needUpdateAfterCooldown]);


    return (
        <div className={classes.mainContainer}>
            <div className={classes.inputTextField}>
                <label htmlFor="input" >Text to replace here</label>
                {<textarea style={{height: "100%", resize: "none"}} placeholder="Text value" ref={inputRef} onChange={(event) => {setInput(event.target.value);}} id="input" type="text" ></textarea>}
            </div>
            <div className={classes.searchingTextField}>
                <label htmlFor="search" >Field to search</label>
                {<textarea style={{height: "100%", resize: "none"}} placeholder="Text value" ref={toSearchRef} onChange={(event) => {setToSearch(event.target.value);}} id="search" type="text" ></textarea>}
            </div>
            <div className={classes.replacingTextField}>
                <label htmlFor="replace" >Field to replace</label>
                {<textarea style={{height: "100%", resize: "none"}} placeholder="Text value" ref={toReplaceRef} onChange={(event) => {setToReplace(event.target.value);}} id="replace" type="text" ></textarea>}
            </div>
            <div className={classes.outputTextField}>
                <label htmlFor="output" >Replaced text here</label>
                {<textarea style={{height: "100%", resize: "none"}} placeholder="Text value" value={String(output)} id="output" type="text" readOnly={true} ></textarea>}
            </div>
        </div>
    )
}
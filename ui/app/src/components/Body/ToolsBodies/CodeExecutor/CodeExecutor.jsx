import classes from "./CodeExecutor.module.css"
import { useState, useRef } from "react";
import AceEditor from "react-ace";
import 'brace/mode/python';
import 'brace/mode/javascript';
import 'brace/mode/json';
import 'brace/theme/github';


export default function CodeExecutor (props) {
    const [input, setInput] = useState("");
    const [output, setOutput] = useState("")

    /*return (
        <div className={classes.mainContainer}>
            <div className={classes.inputTextField}>
                <label htmlFor="input" >Your code here</label>
                {<textarea style={{height: "100%", resize: "none"}} placeholder="Text value" onChange={(event) => {console.log(event.target.value);setInput(event.target.value)}} id="input" type="text" ></textarea>}
            </div>
            <div className={classes.stdoutField}>
                <label htmlFor="output" >Stdout</label>
                {<textarea style={{height: "100%", resize: "none"}} placeholder="Text value" value={output} id="output" type="text" readOnly={true} ></textarea>}
            </div>
            <div className={classes.stderrField}>
                <label htmlFor="output" >Stderr</label>
                {<textarea style={{height: "100%", resize: "none"}} placeholder="Text value" value={output} id="output" type="text" readOnly={true} ></textarea>}
            </div>
        </div>
    )*/
    let globalValue;
    
    const aceEditor = <AceEditor
        mode="python"
        theme="github"
        onChange={(value) => {globalValue=value}}
        name="ace_editor"
        editorProps={{
            $blockScrolling: true,
            useWorker: false
        }} />   
    return (
        <div  className={classes.mainContainer}>
            <div className={classes.inputTextField}>
                <label htmlFor="input" >Text to replace here</label>
                {<textarea style={{height: "100%", resize: "none"}} placeholder="Text value" onChange={(event) => {console.log(event.target.value);setInput(event.target.value)}} id="input" type="text" ></textarea>}
            </div>
            <div className={classes.stdoutField}>
                <label htmlFor="output" >Replaced text here</label>
                {<textarea style={{height: "100%", resize: "none"}} placeholder="Text value" value={output} id="output" type="text" readOnly={true} ></textarea>}
            </div>
                <div id="editor" >
                {aceEditor}
                </div>
                <div>
                <button onClick={() => {console.log(globalValue)}}></button>
            </div>
            </div>
    )
}


/*<body>
        <div id="editor"></div>
        <script src="http://d1n0x3qji82z53.cloudfront.net/src-min-noconflict/ace.js" type="text/javascript" charset="utf-8"></script>
        <script>
            var editor = ace.edit("editor"); // теперь обращаться к редактору будем через editor
            // Далее весь экшон будет проходить тут!
        </script>
    </body>*/
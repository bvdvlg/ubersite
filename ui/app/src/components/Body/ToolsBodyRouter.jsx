import { Route, Routes, Switch } from "react-router-dom"
import TestTool from "./ToolsBodies/TestTool/TestTool"
import Json2Dict from "./ToolsBodies/Json2Dict/Json2Dict"
import CodeExecutor from "./ToolsBodies/CodeExecutor/CodeExecutor"

export default function ToolsBodyRouter(props) {
    console.log("We are here")
    return (
        <Routes>
            <Route exact path="replacer" element={<TestTool />}></Route>
            <Route exact path="json2dict" element={<Json2Dict />} />
            <Route exact path="code_executor" element={<CodeExecutor />} />
            <Route path="*" element={<div>This section is developing</div>}></Route>
        </Routes>
    )
}
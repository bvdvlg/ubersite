import classes from './App.module.css';
import Header from "./components/Header/Header"
import Body from "./components/Body/Body"

import { BrowserRouter } from "react-router-dom";

function App() {
  console.log("REndering app now")
  return (
    <main>
      <BrowserRouter basename="/">
        <Header />
        <Body />
      </BrowserRouter>
      <footer>the foot of page</footer>
    </ main>
  )
}

export default App;

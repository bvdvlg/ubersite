import classes from "./Body.module.css"
import Content from "./Content"

export default function Body (props) {
    return (
        <div className={classes.body}>
            <section id="sidebar" ></section>
            <Content />
            <aside></aside>
        </div>
    )
}
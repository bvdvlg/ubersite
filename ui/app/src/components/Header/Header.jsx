import Navbar from "./Navbar"
import classes from "./Header.module.css"

export default function Header (props) {
    return (
        <>
            <header>
                <div className={classes.navBar}>
                    <Navbar />
                </div>
                <div id={classes.rightCorner} >Bvdvlg tools website</div>
            </header>
        </>
    )
}
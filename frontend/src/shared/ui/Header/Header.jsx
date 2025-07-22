import styles from './Header.module.css';
import logo from '../../assets/logo.png';
import {useScrollHeader} from "./hooks//useScrollHeader.js";

export default function Header() {
    const isScrolled = useScrollHeader();

    return (
        <header className={`${styles.app_header} ${isScrolled ? styles.scrolled : ''}`}>
            <a href="/" className={styles.logo}>
                <img src={logo} alt="Header logo"/>
            </a>

            <nav>
                <ul>
                    <li><a href="/">Главная</a></li>
                </ul>
            </nav>
        </header>
    )
}
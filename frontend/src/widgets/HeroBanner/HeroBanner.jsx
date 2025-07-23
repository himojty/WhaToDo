import Button from "@shared/ui/Button/Button.jsx";
import background from './assets/background-hero.png'
import styles from "./HeroBanner.module.css"

export default function HeroBanner() {
    return (
        <section className={styles.welcome_section}>
            <div className={styles.welcome_text}>
                <h1 className="">Добро пожаловать на <br/><span>WhaToWatch</span></h1>
                <p>Лучший агрегатор фильмов со всего интернета</p>
                <p>Находите, переходите, смотрите</p>


                <a href="/movies">
                    <Button content={'Начать'}/>
                </a>
            </div>
            <img src={background} alt="Кинотеатр с попкорном"/>
        </section>
    )
}
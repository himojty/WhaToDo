import RecomCard from "@widgets/RecomCard/RecomCard.jsx";
import styles from "./GroupReCa_3.module.css";

export default function GroupReCa_3() {
    return (
        <section className={styles.groupSection}>
            <RecomCard CardLogo={'🎬'} CardTitle={'Где посмотреть'}
                       CardContentText={'Узнайте, на каких платформах доступен фильм прямо сейчас'}/>
            <RecomCard CardLogo={'🍿'} CardTitle={'Что посмотреть'}
                       CardContentText={'Персональные рекомендации на основе ваших предпочтений'}/>
            <RecomCard CardLogo={'🔖'} CardTitle={'Поиск по тегам'}
                       CardContentText={'Найдите фильмы по настроению, жанру или ключевым словам'}/>
        </section>
    )
}
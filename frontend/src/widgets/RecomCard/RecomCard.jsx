import Button from "@shared/ui/Button/Button.jsx";
import styles from "./RecomCard.module.css";

export default function RecomCard({CardLogo, CardTitle, CardContentText}) {
    return (
        <div className={styles.RecomCard}>
            <div className={styles.CardLogo}>{CardLogo}</div>
            <h3>{CardTitle}</h3>
            <p>{CardContentText}</p>
            <Button content={'Перейти'}/>
        </div>
    )
}
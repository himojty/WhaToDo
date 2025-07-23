import styles from './Button.module.css'

export default function Button({funcOnClick, content}) {
    return (
        <button className={styles.cta_button} onClick={funcOnClick}>
            {content}
        </button>
    )
}
import {useState} from "react";
import Button from "@shared/ui/Button/Button.jsx";
import styles from "./SearchWidget.module.css";

const SearchWidget = ({onSearch, SearchTitle = "Поиск"}) => {
    const [query, setQuery] = useState('');

    return (
        <section className={styles.searchSection}>
            <h2>{SearchTitle}</h2>
            <div>
                <input
                    type="text"
                    value={query}
                    onChange={(e) => setQuery(e.target.value)}
                    placeholder="Поиск..."
                />
                <Button onClick={() => onSearch(query)} content='Найти'/>
            </div>
        </section>
    );
};

export default SearchWidget;
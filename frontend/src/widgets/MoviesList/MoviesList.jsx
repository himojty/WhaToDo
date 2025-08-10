import {useEffect, useState} from "react";
import styles from './MoviesList.module.css';
import MoviesCard from "@widgets/MovieCard/MovieCard.jsx";

export default function MoviesList() {
    const [movies, setMovies] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);
    const [page, setPage] = useState(0);
    const [hasMore, setHasMore] = useState(true);
    const limit = 20; // Количество фильмов за одну загрузку

    const fetchMovies = async (pageNumber) => {
        try {
            const skip = pageNumber * limit;
            const response = await fetch(`http://127.0.0.1:8000/api/movies/?skip=${skip}&limit=${limit}`);

            if (!response.ok) {
                throw new Error('Не удалось загрузить фильмы');
            }

            const data = await response.json();

            // Если пришло меньше фильмов, чем мы запрашивали, значит это последняя страница
            if (data.length < limit) {
                setHasMore(false);
            }

            return data;
        } catch (err) {
            setError(err.message);
            return [];
        }
    };

    const loadMoreMovies = async () => {
        if (!hasMore) return;

        setLoading(true);
        const nextPage = page + 1;
        const newMovies = await fetchMovies(nextPage);

        setMovies(prev => [...prev, ...newMovies]);
        setPage(nextPage);
        setLoading(false);
    };

    useEffect(() => {
        const loadInitialMovies = async () => {
            const initialMovies = await fetchMovies(0);
            setMovies(initialMovies);
            setLoading(false);
        };

        loadInitialMovies();
    }, []);

    if (error) return <div>Ошибка: {error}</div>;
    if (loading && movies.length === 0) return <div>Загрузка фильмов...</div>;
    if (movies.length === 0) return <div>Фильмы ещё не загрузили</div>;

    return (
        <div className={styles.moviesList}>
            <h1 className={styles.moviesList__title}>Популярные фильмы</h1>
            <div className={styles.moviesGrid}>
                {movies.map((movie) => (
                    <MoviesCard key={movie.id} movie={movie}/>
                ))}
            </div>

            {hasMore && (
                <div className={styles.loadMoreContainer}>
                    <button
                        onClick={loadMoreMovies}
                        disabled={loading}
                        className={styles.loadMoreButton}
                    >
                        {loading ? 'Загрузка...' : 'Загрузить ещё'}
                    </button>
                </div>
            )}
        </div>
    );
}
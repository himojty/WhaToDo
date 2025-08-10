import {useEffect, useState} from 'react';
import {useParams} from 'react-router-dom';
import styles from './MovieSingle.module.css';

export default function MovieSingle() {
    const {id} = useParams();
    const [movie, setMovie] = useState(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        const fetchMovie = async () => {
            try {
                const response = await fetch(`http://127.0.0.1:8000/api/movies/${id}`);

                if (!response.ok) {
                    throw new Error('Фильм не найден');
                }

                const data = await response.json();
                setMovie(data);
            } catch (err) {
                setError(err.message);
            } finally {
                setLoading(false);
            }
        };

        fetchMovie();
    }, [id]);

    if (loading) return (
        <div className={styles.loadingContainer}>
            <div className={styles.spinner}></div>
            <p>Загрузка данных о фильме...</p>
        </div>
    );

    if (error) return (
        <div className={styles.errorContainer}>
            <div className={styles.errorIcon}>⚠️</div>
            <h2>Произошла ошибка</h2>
            <p>{error}</p>
            <button className={styles.retryButton} onClick={() => window.location.reload()}>Попробовать снова</button>
        </div>
    );

    if (!movie) return (
        <div className={styles.notFoundContainer}>
            <div className={styles.notFoundIcon}>🔍</div>
            <h2>Фильм не найден</h2>
            <p>К сожалению, запрашиваемый фильм отсутствует в нашей базе.</p>
        </div>
    );

    return (
        <div className={styles.movieContainer}>
            <div className={styles.movieHeader}>
                <h1 className={styles.movieTitle}>{movie.title}</h1>
                <div className={styles.movieSubtitle}>
                    <span className={styles.originalTitle}>{movie.origin_title}</span>
                    <span className={styles.releaseYear}>({movie.release})</span>
                </div>
            </div>

            <div className={styles.movieContent}>
                <div className={styles.posterContainer}>
                    <img
                        src={`http://localhost:8000/static/movie_images/${movie.image_paths.path.split('\\').pop()}`}
                        alt={movie.title}
                        className={styles.poster}
                    />
                    <div className={styles.ratings}>
                        <div className={styles.ratingItem}>
                            <span className={styles.ratingLabel}>IMDb:</span>
                            <span className={styles.ratingValue}>{movie.ratings?.imdb || '—'}</span>
                        </div>
                        <div className={styles.ratingItem}>
                            <span className={styles.ratingLabel}>Кинопоиск:</span>
                            <span className={styles.ratingValue}>{movie.ratings?.kinopoisk || '—'}</span>
                        </div>
                    </div>
                </div>

                <div className={styles.details}>
                    <div className={styles.descriptionSection}>
                        <h3 className={styles.sectionTitle}>Описание</h3>
                        <p className={styles.descriptionText}>{movie.description}</p>
                    </div>

                    {movie.sites?.length > 0 && (
                        <div className={styles.linksSection}>
                            <h3 className={styles.sectionTitle}>Ссылки для просмотра</h3>
                            <ul className={styles.linksList}>
                                {movie.sites.map((siteItem, index) => (
                                    <li key={index} className={styles.linkItem}>
                                        <a
                                            href={siteItem.site || '#'}
                                            target="_blank"
                                            rel="noopener noreferrer"
                                            className={styles.link}
                                            title={siteItem.site}
                                        >
                                            {siteItem.site ? (
                                                <>
                                <span className={styles.linkDomain}>
                                    {new URL(siteItem.site).hostname.replace('www.', '')}
                                </span>
                                                    <span className={styles.linkPath}>
                                    {new URL(siteItem.site).pathname}
                                </span>
                                                </>
                                            ) : 'Неизвестный сайт'}
                                        </a>
                                    </li>
                                ))}
                            </ul>
                        </div>
                    )}
                </div>
            </div>
        </div>
    );
}
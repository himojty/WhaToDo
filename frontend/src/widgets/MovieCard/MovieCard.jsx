import React from 'react';
import PropTypes from 'prop-types';
import styles from './MovieCard.module.css';
import {Link} from "react-router-dom";

export default function MovieCard({movie}) {
    const getImageUrl = () => {
        if (!movie.image_paths?.path) return null;
        const filename = movie.image_paths.path.split('\\').pop();
        return `http://localhost:8000/static/movie_images/${filename}`;
    };

    const imageUrl = getImageUrl();

    return (
        <Link to={`/movies/${movie.id}`} className={styles.card}>
            <div className={styles.posterContainer}>
                {imageUrl ? (
                    <img
                        src={imageUrl}
                        alt={`Постер ${movie.title}`}
                        className={styles.poster}
                        onError={(e) => {
                            e.target.onerror = null;
                            e.target.classList.add(styles.posterError);
                        }}
                    />
                ) : (
                    <div className={styles.posterPlaceholder}>
                        <span>{movie.title}</span>
                    </div>
                )}
            </div>
        </Link>
    );
}

MovieCard.propTypes = {
    movie: PropTypes.shape({
        id: PropTypes.number.isRequired,
        title: PropTypes.string.isRequired,
        image_paths: PropTypes.shape({
            path: PropTypes.string,
        }),
    }).isRequired,
};
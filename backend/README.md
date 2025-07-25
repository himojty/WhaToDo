# Сущности

Movies:

    - `id`
    - `title`
    - `origin-title`
    - `desription`
    - `release`
    - `image`

    - `tags`
    - `rating`
    - `sites`
    - `age-limit`

Tags:

Связь с `Movies` М к М. У каждого тега может быть много фильмов

    - `id` 
    - `tag`

    - `movie_id` fk

Rating:

Связь с `Movies` 1 к 1. У каждого фильма только по одному парному значению рейтинга относящегося только к нему 

    - `id`
    - `imdb`
    - `kinopoisk`
    
    - `movie_id` fk

Sites:

Связь с `Movies` 1 к 1. У каждого списка сайтов для просмотра только по одному фильму. 
    - `id`
    - `sites`

    - `movie_id` fk

Age-limit:

    - `id`
    - `age-limit`

    - `movie_id` fk
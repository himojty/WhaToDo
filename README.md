# WhaToWatch // W2W
[![Python checks 🐍](https://img.shields.io/github/actions/workflow/status/mahenzon/fastapi-url-shortener/python-checks.yaml?branch=master&label=Python%20checks%20%F0%9F%90%8D&logo=github&style=for-the-badge)](https://github.com/mahenzon/fastapi-url-shortener/actions/workflows/python-checks.yaml)
[![Python Version](https://img.shields.io/badge/python-3.13%2B-blue?logo=python&style=for-the-badge)](https://www.python.org/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg?logo=python&style=for-the-badge)](https://github.com/psf/black)


## Описание проекта

Проект связанный с кино (Где посмотреть? Что посмотреть?).

### Функционал:

- Добавление фильмов/сериалов с оценкой, жанрами, годом выпуска.

- Возможность отмечать просмотренные и добавлять в "буду смотреть".

- Фильтрация по жанрам, году, рейтингу.

- Простая рекомендательная система ("Похожие фильмы").

#### 🎲 "Что посмотреть?"
    
Теги для фильмов:
 - Для поиска

Фильтры:
 - По жанру, году, рейтингу (IMDb/Kinopoisk).
 - "Не смотрел" / "Только новинки".

Рандомайзер:
 - Кнопка "Случайный фильм" (можно с уточнением: "Только комедии", "Не длиннее 2 часов").

Рекомендации:
 - На основе просмотренного ("Похоже на Интерстеллар").
 - Тренды (что сейчас популярно).
        
Фишки:
 - Опрос перед подбором ("Устал(-а) – хочу лёгкое кино" vs "Готов(-а) к сложному сюжету").
 - Подбор по настроению (API ChatGPT для описания запроса).

#### 🎯 Дополнительные фичи

Кино-квизы:
 - Викторины по фильмам (пользовательские и готовые).

Локации:
 - "Где снимали этот фильм?" (интеграция с картами).

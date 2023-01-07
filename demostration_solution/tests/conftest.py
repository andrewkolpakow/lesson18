#файл с фикстурами, pytest автоматически ищет файл с названием conftest
import pytest

from unittest.mock import MagicMock

from setup_db import db
from dao.model.director import Director
from dao.model.genre import Genre
from dao.model.movie import Movie
from dao.director import DirectorDAO
from dao.genre import GenreDAO
from dao.movie import MovieDAO

@pytest.fixture()
def director_dao():
    director_dao = DirectorDAO(db.session)

    director_1 = Director(id=1, name='Tarantino')
    director_2 = Director(id=2, name='Burton')
    director_3 = Director(id=3, name='Spilberg')
    '''Создали псевдо-объекты базы данных, которые будут попадать в тесты'''

    directors = {
        1: director_1,
        2: director_2,
        3: director_3
    }

    director_dao.get_one = MagicMock(return_value=director_1) #предоставляем MagicMock доступ к get_one
    director_dao.get_all = MagicMock(return_value=directors.values())
    director_dao.create = MagicMock(return_value=director_1)
    director_dao.delete = MagicMock()
    director_dao.update = MagicMock()
    '''Предоставляем MagicMock доступ к методам dao, чтобы при тестировании не было обращений к БД'''

    return director_dao

@pytest.fixture()
def genre_dao():
    genre_dao = GenreDAO(db.session)

    genre_1 = Genre(id=1, name='Genre 1')
    genre_2 = Genre(id=2, name='Genre 2')
    genre_3 = Genre(id=3, name='Genre 3')

    genres = {
        1: genre_1,
        2: genre_2,
        3: genre_3
    }

    genre_dao.get_one = MagicMock(return_value=genre_1)  # предоставляем MagicMock доступ к get_one
    genre_dao.get_all = MagicMock(return_value=genres.values())
    genre_dao.create = MagicMock(return_value=genre_1)
    genre_dao.delete = MagicMock()
    genre_dao.update = MagicMock()

    return genre_dao

@pytest.fixture()
def movie_dao():
    movie_dao = MovieDAO(db.session)

    movie_1 = Movie(id=1, title="First Movie", description="Description", trailer="link", year=2000, rating=10.0, genre_id=1, director_id=1)
    movie_2 = Movie(id=2, title="Second Movie", description="Description", trailer="link", year=2010, rating=9.0, genre_id=1, director_id=1)
    movie_3 = Movie(id=2, title="Third Movie", description="Description", trailer="link", year=2010, rating=9.0, genre_id=1, director_id=1)

    movies = {
        1: movie_1,
        2: movie_2,
        3: movie_3
    }

    movie_dao.get_one = MagicMock(return_value=movie_1)  # предоставляем MagicMock доступ к get_one
    movie_dao.get_all = MagicMock(return_value=movies.values())
    movie_dao.create = MagicMock(return_value=Movie(id=1, title='First Movie'))
    movie_dao.delete = MagicMock()
    movie_dao.update = MagicMock()

    return movie_dao
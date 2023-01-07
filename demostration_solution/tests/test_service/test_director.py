import pytest

from service.director import DirectorService

class TestDirectorService:

    @pytest.fixture(autouse=True)
    def director_service(self, director_dao):
        self.director_service = DirectorService(dao=director_dao)
        '''Фикстура для сервиса на базе фикстуры от DAO'''

    def test_get_one(self):
        director = self.director_service.get_one(1)
        assert director is not None
        assert director.id is not None
        assert director.name == "Tarantino"

    def test_get_all(self):
        directors = self.director_service.get_all()
        assert directors is not None
        assert len(directors) > 0

    def test_create(self):
        director_d = {
            "name": "Director 4"
        }

        director = self.director_service.create(director_d)
        assert director.id is not None


    def test_delete(self):
        assert self.director_service.delete(1) is None

    def test_update(self):
        director_d = {
            "id": 1,
            "name": "New Name"
        }

        assert self.director_service.update(director_d) is not None
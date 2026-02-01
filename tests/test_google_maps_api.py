import pytest
from requests import Response
import json

from utils.api import GoogleMapsApi


class TestCreatePlace:

    @pytest.fixture
    def place_id_initialize(self):
        result_post: Response = GoogleMapsApi.create_new_place()
        assert result_post.status_code == 200, f"Неверный статус код: {result_post.status_code}"

        try:
            check_post = result_post.json()
        except json.JSONDecodeError:
            pytest.fail("Ответ не является валидным JSON")

        place_id = check_post.get('place_id')
        assert place_id is not None, "Отсутствует обязательное поле 'place_id'"

        print(f"Создан place_id: {place_id}")
        yield place_id
        print(f"\nЗавершение теста с place_id: {place_id}")

    def test_create_new_place(self, place_id_initialize):
        place_id = place_id_initialize

        print("Метод POST")
        result_post: Response = GoogleMapsApi.create_new_place()
        assert result_post.status_code == 200, f"Неверный статус код: {result_post.status_code}"

        try:
            post_data = result_post.json()
        except json.JSONDecodeError:
            pytest.fail("Ответ не является валидным JSON")

        required_fields = ['place_id', 'status']
        for field in required_fields:
            assert field in post_data, f"Отсутствует обязательное поле '{field}'"

        print('Метод GET POST')
        result_get: Response = GoogleMapsApi.get_new_place(place_id)
        assert result_get.status_code == 200, f"Неверный статус код: {result_get.status_code}"

        try:
            get_data = result_get.json()
        except json.JSONDecodeError:
            pytest.fail("Ответ не является валидным JSON")

    def test_put_new_place(self, place_id_initialize):
        place_id = place_id_initialize

        print('Метод PUT')
        result_put: Response = GoogleMapsApi.put_new_place(place_id)
        assert result_put.status_code == 200, f"Неверный статус код: {result_put.status_code}"

        try:
            put_data = result_put.json()
        except json.JSONDecodeError:
            pytest.fail("Ответ не является валидным JSON")

        print('Метод GET PUT')
        result_get: Response = GoogleMapsApi.get_new_place(place_id)
        assert result_get.status_code == 200, f"Неверный статус код: {result_get.status_code}"

        try:
            get_data = result_get.json()
        except json.JSONDecodeError:
            pytest.fail("Ответ не является валидным JSON")

    def test_delete_place(self, place_id_initialize):
        place_id = place_id_initialize

        print('Метод DELETE')
        result_delete: Response = GoogleMapsApi.delete_new_place(place_id)
        assert result_delete.status_code == 200, f"Неверный статус код: {result_delete.status_code}"

        try:
            delete_data = result_delete.json()
        except json.JSONDecodeError:
            pytest.fail("Ответ не является валидным JSON")

        print('Метод GET DELETE')
        result_get: Response = GoogleMapsApi.get_new_place(place_id)
        assert result_get.status_code == 404, f"Ожидался статус 404, получен: {result_get.status_code}"
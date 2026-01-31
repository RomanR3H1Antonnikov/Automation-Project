from requests import Response

from utils.api import GoogleMapsApi

class TestCreatePlace:

    def test_create_new_place(self):

        print("Метод POST")
        result_post: Response = GoogleMapsApi.create_new_place()
        check_post = result_post.json()
        place_id = check_post.get('place_id')

        print('Метод GET POST')
        result_get: Response = GoogleMapsApi.get_new_place(place_id)

        print('Метод PUT')
        result_put: Response = GoogleMapsApi.put_new_place(place_id)

        print('Метод GET PUT')
        result_get: Response = GoogleMapsApi.get_new_place(place_id)
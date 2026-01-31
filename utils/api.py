from utils.http_methods import HTTPMethods


class GoogleMapsApi:

    base_url = "https://rahulshettyacademy.com"
    key = "?key=qaclick123"

    @classmethod
    def create_new_place(cls):

        json_for_create_new_place = {
            "location": {
                "lat": -38.383494,
                "lng": 33.427362
            }, "accuracy": 50,
                "name": "Frontline house",
                "phone_number":
                    "(+91) 983 893 3937",
                "address": "29, side layout, cohen 09",
                "types": ["shoe park", "shop"],
                "website": "http://google.com",
                "language": "French-IN"
        }

        post_resource = "/maps/api/place/add/json"
        post_url = cls.base_url + post_resource + cls.key
        print(post_url)
        result_post = HTTPMethods.post(post_url, json_for_create_new_place)
        print(result_post.text)
        return result_post


    @classmethod
    def get_new_place(cls, place_id):

        get_resource = "/maps/api/place/get/json"
        get_url = cls.base_url + get_resource + cls.key + "&place_id=" + place_id
        print(get_url)
        result_get = HTTPMethods.get(get_url)
        print(result_get.text)
        return result_get
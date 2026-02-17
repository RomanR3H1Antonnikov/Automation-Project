import json
from requests import Response


class Checking:

    @staticmethod
    def check_status_code(response: Response, status_code):
        assert status_code == response.status_code, f"Провал. Статус код = {response.status_code}, ожидался {status_code}"
        print(f"Успешно. Статус-код равен = {response.status_code}")

    @staticmethod
    def check_json_token(response: Response, expected_value):
        token = json.loads(response.text)
        assert list(token) == expected_value, f"Провал. Поля = {list(token)}, ожидались {expected_value}"
        print("Все поля присутствуют")

    @staticmethod
    def check_json_value(response: Response, field_name, expected_value):
        check = response.json()
        check_info = check.get(field_name)
        assert check_info == expected_value, f"Провал. Значение = {check_info}, ожидалось {expected_value}"
        print(f"{field_name} верен.")

    @staticmethod
    def check_json_search_word_in_value(response: Response, field_name, search_word):
        check = response.json()
        check_info = check.get(field_name)
        assert search_word in check_info, f"Слово {search_word} отсутствует!"
        print(f"Слово {search_word} присутствует")
import requests

from config import captcha_dict_file_id

async def get_random_emoji_for_captcha() -> list:
    
    # Получаем случайное число от random.org
    response = requests.get(
        url = 'https://www.random.org/integers/',
        params = {
            'num': 1,
            'min': 0,
            'max': len(captcha_dict_file_id) - 1,
            'col': 1,
            'base': 10,
            'format': 'plain',
            'rnd': 'new'
        }
    )
    
    # Проверяем, что запрос был успешным
    if response.status_code == 200:
        # Получаем случайное число из ответа
        random_index = int(response.text.strip())
        # Получаем список всех ключей в словаре
        keys = list(captcha_dict_file_id.keys())
        # Выбираем случайный ключ
        random_key = keys[random_index]
        # Возвращаем пару ключ-значение
        return random_key, captcha_dict_file_id[random_key]
    else:
        raise Exception("Ошибка в запросе к random.org")


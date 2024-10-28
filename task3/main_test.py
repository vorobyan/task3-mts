# tests/test_api.py
import pytest
import requests

BASE_URL = 'http://localhost:8000'  # Замените на порт вашего локального сервера


def test_inverse():
    # Подготовка данных для теста
    data = {
        "key1": "value1",
        "key2": "value2"
    }

    # Отправка POST-запроса
    response = requests.post(f'{BASE_URL}/inverse', json=data)

    # Проверка статуса ответа
    assert response.status_code == 200

    # Проверка содержимого ответа
    expected_response = {
        "value1": "key1",
        "value2": "key2"
    }

    assert response.json() == expected_response


def test_unstable():
    happy_count = 0
    unhappy_count = 0
    trials = 10  # Количество попыток

    for _ in range(trials):
        response = requests.get(f'{BASE_URL}/unstable')

        if response.status_code == 200:
            happy_count += 1
            assert response.json() == {"message": "HAPPY"}
        elif response.status_code == 400:
            unhappy_count += 1
            assert response.json() == {"detail": "UNHAPPY"}
        else:
            pytest.fail("Unexpected status code")

    # Проверка, что оба состояния были получены хотя бы раз
    assert happy_count > 0 or unhappy_count > 0

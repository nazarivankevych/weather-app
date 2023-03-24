import requests
import pytest

from main import get_weather


@pytest.fixture
def mock_get(mocker):
    # Create a mock of the requests.get() method
    mock_get = mocker.patch.object(requests, "get")

    # Define the custom response to be returned by the mock object
    custom_response = {
        "status_code": 200,
        "json": lambda: {
            "name": "London",
            "weather": [{"description": "overcast clouds"}],
        },
    }

    # Configure the mock object to return the custom response
    mock_get.return_value = type("mocked_response", (), custom_response)

    yield mock_get


def test_get_weather(mock_get):
    # Call the get_weather() function with any city name
    response = get_weather("any_city_name")

    # Assert that the requests.get() method was called with the correct URL
    mock_get.assert_called_with(
        "https://api.openweathermap.org/data/2.5/weather?q=any_city_name&appid=your_api_key_here"
    )

    # Assert that the function returns the expected data
    assert response.status_code == 200
    assert response.json()["name"] == "London"
    assert response.json()["weather"][0]["description"] == "overcast clouds"

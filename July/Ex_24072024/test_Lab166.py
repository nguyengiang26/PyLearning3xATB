# GET request - Booking ID
# Request (Client - Server): URL, Auth, Payload, Content-Type/Header, Query Parameters, Path Parameters
# Response (Server - Client): Body ( Veridy Assert, Key, Value), Status Code, Time, JSON schema, XML schema
import requests
# import allure
# import pytest

# @allure.title("Test GET request - Restful Booker Project#1")
# @allure.description("Test GET request for Booking ID")
# @allure.tag("regression", "smoke", "p0")
# @allure.label("owner", "QA Team")
# @allure.testcase("TC-001")
# @pytest.mark.smoke
def test_get_single_booking_by_ID():
    url = "https://restful-booker.herokuapp.com/booking/1"
    responseData = requests.get(url)
    print(responseData.text)
    assert responseData.status_code == 200

# @allure.title("Test GET request - Restful Booker Project#1")
# @allure.description("TC2 - Test GET request with invalid booking ID")
# @pytest.mark.smoke
def test_get_single_booking_by_ID_negative():
    url = "https://restful-booker.herokuapp.com/booking/invalid"   # Invalid booking ID
    responseData = requests.get(url)
    print(responseData.text)
    assert responseData.status_code == 404 # Expecting 404 Not Found for invalid booking ID

# @allure.title("Test GET request - Restful Booker Project#1")
# @allure.description("TC3 - Test GET request with invalid booking ID")
# @pytest.mark.smoke
def test_get_single_booking_by_ID_negative2():
    url = "https://restful-booker.herokuapp.com/booking/invalid"   # Invalid booking ID
    responseData = requests.get(url)
    print(responseData.text)
    assert responseData.status_code != 404 # Expecting 404 Not Found for invalid booking ID
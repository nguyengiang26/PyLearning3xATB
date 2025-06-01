import pytest
import requests
import allure

base_url = "https://restful-booker.herokuapp.com"
base_path = "/booking"
URL = base_url + base_path
headers = {"ContenType" : "application/json"}
payload = {
    "firstname": "Jim",
    "lastname": "Brown",
    "totalprice": 111,
    "depositpaid": True,
    "bookingdates": {
        "checkin": "2018-01-01",
        "checkout": "2019-01-01"
    },
    "additionalneeds": "Breakfast"
}

@allure.title("Create Booking CRUD")
@allure.description("TC#1 - Verify the create Booking")
@pytest.mark.crud
def test_create_booking_positive():
    # To make POST request: url, method, header, Payload, Auth(no)
    responseData = requests.post(URL, headers=headers, json=payload)
    responseBody = responseData.json()
    assert responseData.status_code == 200
    
    # Check body
    bookingID = responseBody["bookingid"]
    print(type(bookingID))
    assert bookingID != None and bookingID > 0
    assert responseBody["booking"]["firstname"] == "Jim", "Incorrect firstname in response"
    assert responseBody["booking"]["lastname"] == "Brown", "Incorrect lastname in response"

@allure.title("Create Booking CRUD")
@allure.description("TC#2 - Verify Booking is not created with {} data")
@pytest.mark.crud
def test_create_booking_invalid_body():
    payload = {}
    responseDate = requests.post(url=URL, headers=headers, json=payload)

    assert responseDate.status_code == 400
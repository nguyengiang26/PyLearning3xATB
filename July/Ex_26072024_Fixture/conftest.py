import pytest
import requests
import allure
# Example: if you want to update -> precondition: token, booking id

@pytest.fixture
def create_token():
    url = "https://restful-booker.herokuapp.com/auth" 
    headers = {"Content-Type" : "application/json"}
    payload = {
        "username": "admin",
        "password": "password123"
    }
    response = requests.post(url, headers=headers, json=payload)
    token =  response.json()["token"]
    return token

@pytest.fixture
def create_booking():
    url = "https://restful-booker.herokuapp.com/booking"
    headers = {"Content-Type": "application/json"}
    payload = {
        "firstname" : "Sally",
        "lastname" : "Brown",
        "totalprice" : 10000,
        "depositpaid" : True,
        "bookingdates" : {
            "checkin" : "2025-01-01",
            "checkout" : "2025-03-01"
            },
        "additionalneeds" : "Breakfast"
    }
    response = requests.post(url, headers=headers, json=payload)
    return response
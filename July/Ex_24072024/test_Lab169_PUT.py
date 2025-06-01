import pytest
import requests
import allure

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

def create_booking():
    # Get booking ID
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

    # Assertions
    assert response.status_code == 200
    # Get the response body and verify the JSON, booking ID is not None
    response_body = response.json()
    response_body["bookingid"] != None
    # Extract the booking ID from the response body
    booking_id = response_body["bookingid"]
    print("Create Data: ", response_body)
    return booking_id

def log_api(response, payload=None):
    if payload:
        allure.attach(str(payload), name="Request Body", attachment_type=allure.attachment_type.JSON)
        allure.attach(response.text, name="Response Body", attachment_type=allure.attachment_type.JSON)
        allure.attach(str(response.status_code), name="Status Code", attachment_type=allure.attachment_type.TEXT)

def test_put_request_positive():
    base_url = "https://restful-booker.herokuapp.com/"
    base_path = "booking/" + str(create_booking())
    put_url = base_url + base_path

    cookie = "token=" + create_token()
    headers = {
        "Content-Type": "application/json",
        "Cookie": cookie
    }
    payload = {
        "firstname": "Sally_updated",
        "lastname": "Brown",
        "totalprice": 10000,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2025-01-01",
            "checkout": "2025-03-01"
        },
        "additionalneeds": "Breakfast"
    }

    response = requests.put(put_url, headers=headers, json=payload)
    
    assert response.status_code == 200
    print("Update Data: ", response.json())
    
    log_api(response, payload)

def test_delete_request_positive():
    url = "https://restful-booker.herokuapp.com/"
    booking_id = create_booking()
    delete_url = url+ str(booking_id)

    cookie = "token=" + create_token()
    response = requests.delete(delete_url, headers={"Cookie": cookie})


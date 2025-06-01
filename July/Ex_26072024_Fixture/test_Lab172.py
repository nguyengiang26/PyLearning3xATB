# import conftest #

def test_create_booking_positive(create_booking):
    assert create_booking.status_code == 200

# def test_create_booking_JSON_invalid(create_booking):
#     payload = {}
#     create_booking = conftest.create_booking(payload)

# def test_update_booking():
#     base_url = "https://restful-booker.herokuapp.com/"
#     base_path = "booking/" + str(create_booking())
#     put_url = base_url + base_path

#     cookie = "token=" + create_token()
#     headers = {
#         "Content-Type": "application/json",
#         "Cookie": cookie
#     }
#     payload = {
#         "firstname": "Sally_updated",
#         "lastname": "Brown",
#         "totalprice": 10000,
#         "depositpaid": True,
#         "bookingdates": {
#             "checkin": "2025-01-01",
#             "checkout": "2025-03-01"
#         },
#         "additionalneeds": "Breakfast"
#     }

#     response = requests.put(put_url, headers=headers, json=payload)
# # Test Update positive 2


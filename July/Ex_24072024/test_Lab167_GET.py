import pytest
import requests
import allure

@allure.title("Test GET request - Restful Booker Project#1")
@allure.description("Test GET request for Booking ID")
@allure.tag("regression", "smoke", "p0")
@allure.label("owner", "QA Team")
@allure.testcase("TC-005")
@pytest.mark.smoke
def test_get_single_booking_by_ID():
    url = "https://restful-booker.herokuapp.com/booking/1"
    responseData = requests.get(url)
    print(responseData)
    
    print("Headers (Return Dict):", responseData.headers)
    print("Get Headers content directly:", responseData.headers["Content-Type"]) # Return Keyerror nếu không có Content-Type
    print("Get Headers using get():", responseData.headers.get("Content-Type","")) 
    

    print("Status code:", responseData.status_code)
    
    print("Text body: Body content in JSON string", responseData.text)
    print("JSON body:", responseData.json())
    print("Content: Body content in bytes, useful when work with file/image", responseData.content)
    
    print("OK? (Return True if status code < 400):", responseData.ok)
    print("Status Reason:", responseData.reason)
    print("URL:", responseData.url)
    print("Cookies:", responseData.cookies)
    print("Encoding:", responseData.encoding)
    print("Elapsed: Response time (datatype: timedata)", responseData.elapsed)
    print("Redirect history:", responseData.history)


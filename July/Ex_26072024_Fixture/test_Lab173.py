from dotenv import load_dotenv
import os


def test_update_request():
    load_dotenv()
    url = os.getenv("URL")
    username = os.getenv("USERNAME")
    password = os.getenv("password")

    # print(url)
    print(username)
    # print(password)

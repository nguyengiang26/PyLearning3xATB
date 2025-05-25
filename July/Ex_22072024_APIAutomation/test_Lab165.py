import pytest
import allure

@pytest.mark.smoke
@allure.title("TC#1 - Verify 0 - 0 =0")
@allure.description("This test verifies that the subtraction of 0 from 0 equals 0")
def test_sub0():
    assert 0-0 == 0

@pytest.mark.regression
@allure.title("TC#1 - Verify 1 - 1 =0")
@allure.description("This test verifies that the subtraction of 1 from 1 equals 0")
def test_sub1():
    assert 1-1 == 0

@pytest.mark.smoke
@allure.title("TC#1 - Verify 2 - 2 =0")
@allure.description("This test verifies that the subtraction of 2 from 2 equals 0")
def test_sub2():
    assert 2-2 == 0

@pytest.mark.skip(reason="Not implemented")
def test_sub3():
    assert 3-3 == 0
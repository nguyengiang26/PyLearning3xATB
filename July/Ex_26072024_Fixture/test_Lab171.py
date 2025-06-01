# Fixture - Concept of Python
# You can use te fixture - multiple task
# provide context to the test (Precondition, post condition), pass data to the test


import pytest

@pytest.fixture()
def is_married():
    return True

def test_I_need_confirm(is_married):
    assert is_married() == True
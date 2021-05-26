import pytest

@pytest.yield_fixture()
def setUp():
    print("Opening URL to Login")
    yield
    print("CLosing browser After Login")

def test_loginbyEmail(setUp):
    print("This is login by email test")

def test_loginbyFacebook(setUp):
    print("This is login by fb test")

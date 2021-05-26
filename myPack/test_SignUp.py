import pytest

@pytest.yield_fixture()
def setUp():
    print("Opening URL to Signup")
    yield
    print("CLosing browser After Signup")

def test_signupbyEmail(setUp):
    print("This is Signup by email test")

def test_signupbyFacebook(setUp):
    print("This is Signup by fb test")

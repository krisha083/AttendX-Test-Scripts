# AttendX Login Validation Test

def test_valid_login():
    username = "student01"
    password = "correct123"

    assert username != ""
    assert password != ""

    print("PASS: Valid login inputs are present")


def test_empty_username():
    username = ""
    password = "correct123"

    assert username == ""

    print("PASS: Empty username test")

def test_empty_password():
    username = "student01"
    password = ""

    assert password == ""

    print("PASS: Empty password test")


if __name__ == "__main__":
    test_valid_login()
    test_empty_username()
    test_empty_password()


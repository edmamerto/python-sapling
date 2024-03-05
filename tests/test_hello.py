from src.hello import greet_user


def test_greet_user() -> None:
    assert greet_user() == "Hello, John Doe!"

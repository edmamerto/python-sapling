from src.hello import say_hello


def test_say_hello() -> None:
    assert say_hello() == "Hello, World!"

from src.models import User


def greet_user() -> str:
    user = User(id=1, name="John Doe", email="john.doe@example.com")
    return f"Hello, {user.name}!"

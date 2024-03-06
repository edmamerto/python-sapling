from src.log import get_logger
from src.models import User

# name of the current module
logger = get_logger(__name__)


def greet_user() -> str:
    user = User(id=1, name="John Doe", email="john.doe@example.com")
    logger.debug("Greeting user", user_id=user.id, user_name=user.name)
    return f"Hello, {user.name}!"

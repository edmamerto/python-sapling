from src.config import initialize_config
from src.hello import greet_user


def main() -> None:
    initialize_config()
    print(greet_user())


if __name__ == "__main__":
    main()

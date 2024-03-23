# Motivation

During my time at "Company X", we had this concept called saplings. Essentially, a sapling serves as a **starting point for development**, much like a young tree 🌱 sprouting from a seed, making it easy for anyone in the company to start a project without having to set everything up from scratch.

I've adopted some of the tools I liked and used them in my personal projects, which is why I'm creating templates now.

>Shoutout to Bruce for influencing many of these tool choices.

# Toolset

|      | Tool       | Type                     | Notes                                                                                                                                                                     |
|:----------:|:-----------|:-------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ✨         | [Poetry](https://python-poetry.org/)     | Dependency Manager       | This is simply a matter of personal taste. I like the modern feel poetry over other dependency managers.                                                                  |
| 🔍         | [Pydantic](https://docs.pydantic.dev/latest/)   | Data Validator           | I like the ease of use and ability to handle complex data validation                                                                                                      |
| 🔄         | [Pre-commit](https://pre-commit.com/) | Automated Checker        | While some individuals dislike this practice due to its disruption of workflow, personally, I appreciate the idea of identifying issues early in the development process. |
| 🚨         | [Flake8](https://flake8.pycqa.org/en/latest/)     | Linter                   | This will always remind me of PEP8, before it was named pycodestyle.                                                                                                      |
| ⬛         | [Black](https://black.readthedocs.io/en/stable/)      | Code Formatter           | Automatically organizes your code while you focus on logic, ensuring your code looks beautiful and consistent.                                                            |
| 🔤         | [Isort](https://pycqa.github.io/isort/)      | Import Statements Sorter | Makes sure my import statements are always in alphabetical order                                                                                                          |
| 📝         | [Structlog](https://www.structlog.org/en/stable/)  | Structured Logging       | Structlog makes it simple for your application's logs to be understood by log management tools when your apps go to production                                            |
| 🧪         | [Mypy](https://mypy.readthedocs.io/en/stable/)       | Type Checker             | Never forget to add type hints with this tool. Compared to the type checkers from big companies like MAANG, I found this one simple to use.                               |
| 🐳         | [Docker](https://www.docker.com/)     | Containerizer            | While poetry introduces an isolation layer, containers simplifies the transfer of your application to various servers.                                                        |
| ✅ | [Pytest](https://docs.pytest.org/en/8.0.x/) | Unit testing | Seems to be the de facto choice for writing tests |
| 💯 | [Pytest-Cov](https://pypi.org/project/pytest-cov/) | Code Coverage | if you use pytest then you should use `pytest-cov` |

# Pre-requisites

Install **poetry**
```
$ pip instll poetry
```
Optionally, You need to have **docker** installed

# Setup
Install dependencies
```bash
$ poetry install
```
Install pre-commit hooks
```bash
$ poetry run pre-commit install
```

# Poetry run
To run the app
```bash
$ poetry run main
```
To run test
```bash
$ poetry run test
```
# Docker run
Build image. Unit testing is run as part of the build process.
```bash
$ docker build -t python-sapling .
```
Run container
```bash
$ docker run python-sapling
```

# Seed
This project was initialized with `poetry`
```bash
$ poetry new my_project_name
```
> This is informational and not part of the setup procedure

## License
**MIT**, or whatever. Feel free to 🍴 it and have fun!

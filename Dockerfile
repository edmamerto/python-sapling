# Use Python 3.11 base image
FROM python:3.11-slim

# Set environment variables

# This environment variable instructs Python not to write bytecode files (.pyc) to disk.
# Bytecode files are typically used to speed up subsequent imports of the same module,
# but in containerized environments or when filesystems are considered ephemeral,
# writing bytecode files can be unnecessary and may cause issues.
ENV PYTHONDONTWRITEBYTECODE 1

# This environment variable ensures that Python's standard output (stdout) and standard error (stderr)
# streams are unbuffered, meaning that the output is immediately flushed to the output stream.
# In containerized environments, buffering can cause delays in output being displayed or logged,
# so setting this variable to a non-empty value (typically '1') helps ensure prompt and correct output behavior.
ENV PYTHONUNBUFFERED 1

# Set working directory in the container
WORKDIR /app

# Copy poetry.lock and pyproject.toml files
COPY poetry.lock pyproject.toml /app/

# Install dependencies
RUN pip install poetry && \
    # Configure Poetry not to create virtual environments
    poetry config virtualenvs.create false && \
    poetry install --no-dev --no-interaction --no-ansi

# Copy the whole project
COPY . /app/

# Run unit tests
RUN poetry run test

# Command to run the application
ENTRYPOINT ["poetry", "run", "python", "main.py"]

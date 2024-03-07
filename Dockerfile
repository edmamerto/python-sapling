# Stage 1: Build dependencies and run tests
FROM python:3.11-slim AS builder

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set working directory in the container
WORKDIR /app

# Create a non-privileged user
RUN adduser --disabled-password --gecos '' appuser

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

# Stage 2: Run the application
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set working directory in the container
WORKDIR /app

# Copy installed dependencies from the previous stage
COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages

# Copy the application code
COPY --from=builder --chown=appuser:appuser /app /app

# Change to non-privileged user
USER appuser

# Command to run the application
ENTRYPOINT ["poetry", "run", "python", "main.py"]

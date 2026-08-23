# OpenCanal

Open-source platform for irrigation canal monitoring using satellite imagery and AI.

## Development

### Run locally with Docker

Run:

    docker compose up --build

The API will be available at:

    http://localhost:8000

Health check:

    http://localhost:8000/health

### Run tests

Create/activate the Python virtual environment, then run:

    python -m pytest

### Run the linter

Run:

    ruff check .

### CI

OpenCanal uses GitHub Actions to automatically:

1. Install Python dependencies
2. Run the pytest test suite
3. Run Ruff linting

Every push to `main` is checked by a temporary Ubuntu Linux runner.

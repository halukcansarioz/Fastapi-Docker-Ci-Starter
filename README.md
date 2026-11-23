# fastapi-docker-ci-starter

[![CI](../../actions/workflows/ci.yml/badge.svg)](../../actions/workflows/ci.yml)

Production-ready FastAPI microservice template with automated `pytest` API tests, Docker containerization, and GitHub Actions CI.

## API Endpoints

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `GET` | `/health` | Health check returning `{"status": "ok"}` |
| `POST` | `/items` | Create a new item (`name`, optional `description`, `price`) |
| `GET` | `/items/{item_id}` | Retrieve an item by its ID |

### Example Request (`POST /items`)

```json
{
  "name": "Sample Item",
  "description": "Optional description",
  "price": 19.99
}
```

## Local Setup

1. Clone the repository:
   ```bash
   git clone git@github.com:halukcansarioz/fastapi-docker-ci-starter.git
   cd fastapi-docker-ci-starter
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Start the development server:
   ```bash
   uvicorn app.main:app --reload
   ```
   The API will be available at `http://localhost:8000` (interactive docs at `http://localhost:8000/docs`).

## Running Tests

Run the automated test suite with `pytest`:
```bash
pytest
```

## Running with Docker

1. Build the Docker image:
   ```bash
   docker build -t fastapi-docker-ci-starter .
   ```

2. Run the container:
   ```bash
   docker run -p 8000:8000 fastapi-docker-ci-starter
   ```
   The service will be accessible at `http://localhost:8000`.

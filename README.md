# ⚡ FastAPI Docker CI Starter

[![CI](../../actions/workflows/ci.yml/badge.svg)](../../actions/workflows/ci.yml)
![Python](https://img.shields.io/badge/Python-3.11-3776AB?logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?logo=fastapi&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?logo=docker&logoColor=white)
![pytest](https://img.shields.io/badge/pytest-0A9EDC?logo=pytest&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green.svg)

---

A production-ready FastAPI starter template featuring containerized deployment with Docker, automated `pytest` suites, and a continuous integration pipeline via GitHub Actions.

---

# 📝 Table of Contents
- [About the Project](#-about-the-project)
- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Installation & Usage](#-installation--usage)
- [Project Structure](#-project-structure)
- [License](#-license)

---

# 📌 About the Project

**FastAPI Docker CI Starter** provides a clean, minimal, and extensible foundation for building RESTful APIs with Python and FastAPI. It comes pre-configured with core health and item endpoints, automated API tests, a `Dockerfile` for reproducible builds, and a GitHub Actions CI workflow that verifies every push and pull request.

---

# ✨ Features

- ✅ **Health Check Endpoint (`GET /health`)** — Returns service status for liveness and readiness probes.
- ✅ **Item Management (`POST /items`, `GET /items/{item_id}`)** — Create and retrieve items with Pydantic request/response validation.
- ✅ **Automated Testing (`pytest`)** — Unit and endpoint integration tests under `tests/test_api.py`.
- ✅ **Docker Support** — Containerized application setup via `Dockerfile` for consistent local and cloud deployments.
- ✅ **GitHub Actions CI** — Automated test execution pipeline defined in `.github/workflows/ci.yml`.

---

# 🛠 Tech Stack

| Category | Technology | Purpose |
| :--- | :--- | :--- |
| **API Framework** | FastAPI | High-performance async REST API & OpenAPI docs |
| **ASGI Server** | Uvicorn | Lightning-fast ASGI server for running FastAPI |
| **Language** | Python 3.11 | Core backend runtime |
| **Testing** | pytest | Automated API endpoint and logic testing |
| **Containerization** | Docker | Reproducible image builds and deployment |
| **CI/CD** | GitHub Actions | Automated test pipeline on push & pull requests |

---

# ⚙️ Installation & Usage

### 1. Local Setup

```bash
git clone git@github.com:halukcansarioz/fastapi-docker-ci-starter.git
cd fastapi-docker-ci-starter
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000` (interactive Swagger docs at `http://localhost:8000/docs`).

### 2. Running Tests

```bash
pytest
```

### 3. Running with Docker

```bash
docker build -t fastapi-docker-ci-starter .
docker run -p 8000:8000 fastapi-docker-ci-starter
```

The containerized service will be accessible at `http://localhost:8000`.

---

# 📁 Project Structure

```text
fastapi-docker-ci-starter/
├── .github/
│   └── workflows/
│       └── ci.yml          # GitHub Actions CI workflow
├── app/
│   └── main.py             # FastAPI application (/health, /items)
├── tests/
│   └── test_api.py         # pytest endpoint test suite
├── Dockerfile              # Container build configuration
├── LICENSE                 # MIT License
├── README.md               # Project documentation
└── requirements.txt        # Python dependencies
```

---

# 📜 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

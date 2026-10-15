#  FastAPI & PostgreSQL Docker Application

A simple yet fully functional REST API application written in FastAPI using SQLAlchemy, integrated with a PostgreSQL database and containerized with Docker. The project is ready for deployment on free hosting platforms (e.g., Render).

Below is an example of deployed application endpoints and docs:

## https://fastapi-postgres-dock.onrender.com/docs

### Tech Stack
* Backend [FastAPI](https://fastapi.tiangolo.com/) (Python 3.13)
* Database [PostgreSQL](https://www.postgresql.org/)
* ORM [SQLAlchemy](https://www.sqlalchemy.org/)
* Database Driver [psycopg (v3)](https://www.psycopg.org/psycopg3/)
* Containerization [Docker](https://www.docker.com/)
* Server [Uvicorn](https://www.uvicorn.org/)

###  Project Structure
```text
fastapi-postgres-dock/
│
├── main.py         # Main API entry points (FastAPI endpoints)
├── models.py       # Database table models (SQLAlchemy)
├── schemas.py      # Data validation schemas (Pydantic)
├── services.py     # Business logic and database operations
├── database.py     # Database connection configuration
├── Dockerfile      # Production Docker image configuration
├── requirements.txt# Python dependencies
└── README.md       # Project documentation

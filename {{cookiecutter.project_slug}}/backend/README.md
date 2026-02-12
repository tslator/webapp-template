# {{ cookiecutter.project_name }} - FastAPI Backend

Backend API built with FastAPI, SQLAlchemy, and PostgreSQL.

## Features

- **Async Python** - Full async/await support for high concurrency
- **Type Hints** - Complete type annotations with mypy
- **Pydantic Validation** - Automatic request/response validation
- **SQLAlchemy ORM** - Powerful database access with async support
- **Alembic Migrations** - Version control for your database schema
- **Dependency Injection** - Clean dependency management
- **CORS Support** - Configurable cross-origin requests
- **Error Handling** - Centralized exception handling
- **Testing** - pytest with fixtures and async support
- **OpenAPI Docs** - Automatic API documentation

## Running the Backend

### With Docker
```bash
cd backend
docker build -t myapp-backend .
docker run -p 8000:8000 myapp-backend
```

### Locally
```bash
cd backend

# Install dependencies
uv sync

# Run migrations
alembic upgrade head

# Start development server
uv run uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

## API Endpoints

- `GET /` - Root endpoint
- `GET /health` - Health check
- `POST /api/users` - Create user
- `GET /api/users` - List users
- `GET /api/users/{id}` - Get user
- `PUT /api/users/{id}` - Update user
- `DELETE /api/users/{id}` - Delete user

Full documentation available at `/docs` when running.

## Database

The backend uses PostgreSQL by default. Configure the connection in `.env`:

```bash
DATABASE_URL=postgresql+asyncpg://user:password@localhost:5432/dbname
```

### Migrations

```bash
# Create new migration
alembic revision --autogenerate -m "Description"

# Apply migrations
alembic upgrade head

# Rollback migration
alembic downgrade -1
```

## Testing

```bash
# Run all tests
uv run pytest

# Run with coverage
uv run pytest --cov=app --cov-report=html

# Run specific test file
uv run pytest tests/unit/test_services.py

# Run with verbose output
uv run pytest -v
```

## Code Quality

```bash
# Lint
uv run ruff check .

# Format
uv run ruff format .

# Type check
uv run mypy app/
```

## Configuration

Environment variables in `.env`:

- `DEBUG` - Debug mode (True/False)
- `DATABASE_URL` - Database connection string
- `JWT_SECRET_KEY` - Secret key for JWT tokens
- `CORS_ORIGINS` - List of allowed CORS origins
- `LOG_LEVEL` - Logging level

## Project Structure

```
backend/
├── app/
│   ├── main.py           # Application factory
│   ├── config.py         # Settings and configuration
│   ├── api/
│   │   ├── routes/       # API endpoints
│   │   └── schemas/      # Pydantic models
│   ├── models/           # SQLAlchemy models
│   ├── database/         # Database session and config
│   ├── services/         # Business logic
│   ├── middleware/       # Middleware (CORS, etc.)
│   └── tests/
│       ├── unit/         # Unit tests
│       ├── integration/  # Integration tests
│       └── fixtures/     # Test data
├── migrations/           # Alembic migrations
├── pyproject.toml        # Dependencies
├── .env.example          # Environment template
└── Dockerfile            # Container definition
```

## Dependencies

Key dependencies:

- **fastapi** - Web framework
- **uvicorn** - ASGI server
- **sqlalchemy** - ORM
- **alembic** - Database migrations
- **pydantic** - Data validation
- **psycopg2** - PostgreSQL driver

Development dependencies:

- **pytest** - Testing framework
- **ruff** - Linting and formatting
- **mypy** - Type checking

See `pyproject.toml` for complete list.

## Performance

Tips for production:

1. Use a production ASGI server (Gunicorn, Duvicorn)
2. Enable connection pooling in SQLAlchemy
3. Use Redis for caching
4. Enable GZIP compression
5. Use CDN for static assets
6. Monitor with application performance monitoring (APM)

## Security

- Always use HTTPS in production
- Set strong values for secrets in `.env`
- Enable CORS only for trusted origins
- Validate and sanitize all inputs
- Use environment variables for sensitive data
- Keep dependencies updated

## Support

See the main README.md for project documentation.

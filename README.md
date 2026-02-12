# Python Web Application Cookie-Cutter Template

A production-ready cookie-cutter template for building modern Python web applications with **FastAPI**, **SQLAlchemy**, **HTMX**, and **Tailwind CSS**.

## Features

✨ **Modern Stack**
- FastAPI - Async Python web framework
- SQLAlchemy 2.0 - Powerful ORM with async support
- Pydantic - Type-safe data validation
- HTMX - Lightweight frontend interactivity
- Tailwind CSS - Utility-first CSS framework

🚀 **Development Ready**
- Docker & Docker Compose - Local and production environments
- Pre-commit hooks - Automated code quality
- Comprehensive testing - Unit, integration, and E2E
- GitHub Actions CI/CD - Automated pipelines
- Database migrations - Alembic version control

🔧 **Developer Experience**
- Type hints - Full type annotation support
- Linting & formatting - Ruff for code quality
- Hot reload - Auto-refresh during development
- Makefile - Common commands simplified
- Comprehensive docs - Multiple README files

## Quick Start

### Installation

```bash
pip install cookiecutter
cookiecutter gh:{{ cookiecutter.github_username }}/webapp-template
```

Or from a local copy:

```bash
cookiecutter ./webapp-template
```

**NOTE: This project assumes `make` is installed.  For Windows, `choco install make`**

**Node.js & npm** are required for frontend development (Tailwind CSS, Vite, HTMX tooling). Download from https://nodejs.org if you need the frontend UI. Backend can run without Node.js.

### After Generation

```bash
cd <your-project-slug>
make install      # Install dependencies
make dev          # Run with Docker Compose
```

Then visit:
- Frontend: `http://localhost:3000`
- Backend API: `http://localhost:8000`
- API Docs: `http://localhost:8000/docs`

### Windows Setup Notes

On Windows, `make install` may fail when building C extensions (for example `greenlet`, `psycopg`). The template defaults to **Python 3.12** which has better wheel availability. The template uses `greenlet>=3.0.3` which has wheels for Python 3.12 and 3.13.

If you encounter build failures:

**Option 1: Clear the uv cache** (Usually fixes the issue)
```powershell
make clean-cache
make install
```

**Option 2: Install Visual C++ Build Tools** (Required for source builds)
- Download from https://visualstudio.microsoft.com/visual-cpp-build-tools/
- Run the installer and select "Desktop development with C++"
- Restart and try `make install` again

**Option 3: Use Python 3.12** (Default)
- The template defaults to Python 3.12 which has prebuilt wheels for all dependencies
- Install from https://www.python.org/downloads/

**Option 4: Use conda** (Easy on Windows)
```bash
conda create -n myapp python=3.12
conda activate myapp
# Then run make install
```

If you see errors mentioning `greenlet`, `cl.exe`, or `pg_config`, try one of the above options.

## Template Options

When generating a project, you'll be prompted for:

- **project_name** - Full name of your project
- **project_slug** - URL-safe project identifier
- **author_name** - Your name
- **author_email** - Your email
- **description** - Project description
- **python_version** - Python version (default: 3.12 for better wheel compatibility)
- **use_docker** - Include Docker support (recommended)
- **use_postgresql** - PostgreSQL database (vs SQLite)
- **use_redis** - Redis caching
- **use_sqlite** - Use SQLite instead of PostgreSQL
- **github_username** - Your GitHub username

## Generated Project Structure

```
my-project/
├── backend/              # FastAPI application
│   ├── app/
│   │   ├── main.py      # Application factory
│   │   ├── config.py    # Configuration
│   │   ├── api/         # Routes and schemas
│   │   ├── models/      # Database models
│   │   └── tests/       # Tests
│   ├── migrations/      # Alembic migrations
│   └── Dockerfile
├── frontend/             # HTMX + Tailwind frontend
│   ├── templates/       # HTML templates
│   ├── static/          # CSS, JS, images
│   └── Dockerfile
├── tests_e2e/           # Playwright E2E tests
├── docker-compose.yml   # Multi-service setup
├── Makefile             # Development commands
├── .pre-commit-config.yaml  # Git hooks
└── .github/workflows/   # CI/CD pipelines
```

## Development Commands

```bash
make help              # Show all commands
make install           # Install dependencies
make dev               # Run with Docker
make dev-local         # Run locally
make test              # Run all tests
make lint              # Check code quality
make format            # Format code
make migrate           # Run database migrations
make build             # Build Docker images
```

## Key Files

### Frontend
- `frontend/templates/base.html` - Base template with HTMX and Tailwind
- `frontend/static/` - CSS, JavaScript, and images
- `frontend/tailwind.config.js` - Tailwind configuration
- `frontend/package.json` - Frontend dependencies

### Backend
- `backend/app/main.py` - FastAPI application factory
- `backend/app/config.py` - Configuration management
- `backend/app/models/` - SQLAlchemy ORM models
- `backend/app/api/` - API routes and Pydantic schemas
- `backend/migrations/` - Alembic database migrations
- `backend/pyproject.toml` - Python dependencies (uv)

### DevOps
- `docker-compose.yml` - Local development services
- `Dockerfile` (backend) - FastAPI container
- `Dockerfile` (frontend) - Nginx container
- `.github/workflows/` - CI/CD pipelines
- `.pre-commit-config.yaml` - Code quality hooks

## Technology Stack

### Backend
- FastAPI 0.115+
- SQLAlchemy 2.0+
- Pydantic 2.0+
- Alembic (migrations)
- Uvicorn (ASGI server)
- psycopg (PostgreSQL driver, binary wheels)
- greenlet (async SQLAlchemy support, binary wheels preferred)
- aiosqlite (async SQLite support)

### Frontend
- HTMX 1.9+
- Tailwind CSS 3.3+
- Vite (build tool)

### Development
- Python 3.12+ (3.14 supported with build tools)
- uv (package manager)
- pytest (testing)
- Ruff (linting/formatting)
- mypy (type checking)
- pre-commit (git hooks)
- Playwright (E2E testing)
- GitHub Actions (CI/CD)

### DevOps
- Docker & Docker Compose
- PostgreSQL 16
- Redis 7 (optional)

## Testing

The generated project includes testing infrastructure:

- **Unit Tests** (`tests/unit/`) - Fast, isolated tests
- **Integration Tests** (`tests/integration/`) - API tests with database
- **E2E Tests** (`tests_e2e/`) - Full user workflows with Playwright

```bash
make test              # Run all tests
make test-unit         # Unit tests only
make test-integration  # Integration tests only
make test-e2e          # E2E tests only
make test-coverage     # Coverage report
```

## CI/CD

GitHub Actions automatically:
- Lint code with Ruff
- Type-check with mypy
- Run all tests with coverage
- Run E2E tests
- Build Docker images
- Generate coverage reports

Modify `.github/workflows/ci.yml` for your needs.

## Deployment

The project is ready for common deployment targets:

### Docker Hub
```bash
docker build -t username/myapp:latest ./backend
docker push username/myapp:latest
docker build -t username/myapp-frontend:latest ./frontend
docker push username/myapp-frontend:latest
```

### Kubernetes
```bash
kubectl apply -f k8s/
```

### Traditional Servers
```bash
# Pull latest code
git pull

# Run migrations
alembic upgrade head

# Restart service
systemctl restart myapp
```

## Environment Variables

Each generated project includes `.env.example` with all required variables. Copy to `.env` and customize:

```bash
cp backend/.env.example backend/.env
```

## Database

Supported databases (via SQLAlchemy):
- **PostgreSQL** (recommended)
- **MySQL / MariaDB**
- **SQLite** (development only)

Database migrations use Alembic for version control.

## Contributing to the Template

To improve this template:

1. Fork the repository
2. Create a feature branch
3. Make improvements
4. Test by generating a project
5. Submit a pull request

## Troubleshooting

### Port Already in Use
```bash
# Change ports in docker-compose.yml or .env
lsof -i :8000
# Kill the process or change port
```

### Database Connection Error
```bash
# Verify PostgreSQL is running and credentials are correct
docker-compose logs postgres
```

### Pre-commit Hook Issues
```bash
# Reinstall pre-commit hooks
pre-commit install --force-all
```

## License

This template is licensed under the MIT License.

## Author

Created by {{ cookiecutter.github_username }}

## Support

For issues, questions, or suggestions:
- [Open an issue on GitHub](https://github.com/{{ cookiecutter.github_username }}/webapp-template/issues)
- Check the documentation in generated projects
- Review the example code in the template

## Related Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org)
- [HTMX Documentation](https://htmx.org)
- [Tailwind CSS Documentation](https://tailwindcss.com)
- [Docker Documentation](https://docs.docker.com)

---

Built with ❤️ for Python developers

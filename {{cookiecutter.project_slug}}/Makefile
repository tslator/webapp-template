.PHONY: help install dev dev-local test test-unit test-e2e lint format type-check clean build migrate seed

# Default target
help:
	@echo "{{ cookiecutter.project_name }} - Development Commands"
	@echo "================================================="
	@echo ""
	@echo "Setup & Installation:"
	@echo "  make install          - Install all dependencies"
	@echo "  make setup            - Initial project setup"
	@echo ""
	@echo "Development:"
	@echo "  make dev              - Run with Docker Compose"
	@echo "  make dev-local        - Run locally without Docker"
	@echo ""
	@echo "Testing:"
	@echo "  make test             - Run all tests"
	@echo "  make test-unit        - Run unit tests only"
	@echo "  make test-integration - Run integration tests"
	@echo "  make test-e2e         - Run E2E tests with Playwright"
	@echo ""
	@echo "Code Quality:"
	@echo "  make lint             - Run Ruff linting"
	@echo "  make format           - Format code with Ruff"
	@echo "  make type-check       - Run mypy type checking"
	@echo "  make quality          - Run all quality checks"
	@echo ""
	@echo "Database:"
	@echo "  make migrate          - Run database migrations"
	@echo "  make migrate-create   - Create new migration"
	@echo "  make seed             - Seed database with sample data"
	@echo ""
	@echo "Docker:"
	@echo "  make build            - Build Docker images"
	@echo "  make build-backend    - Build backend image only"
	@echo "  make build-frontend   - Build frontend image only"
	@echo ""
	@echo "Cleanup:"
	@echo "  make clean            - Clean build artifacts and cache"
	@echo "  make clean-docker     - Remove Docker containers and volumes"
	@echo "  make clean-cache      - Clear uv package manager cache"
	@echo "  make clean-all        - Clean everything"

# Installation
install:
	@echo "Installing dependencies..."
	@python -m pip install --upgrade pip setuptools wheel || true
	cd backend && uv sync || ( \
		echo "ERROR: backend install failed." >&2; \
		echo "This often happens when downloading prebuilt wheels fails." >&2; \
		echo "Try clearing the uv cache: uv cache clean" >&2; \
		echo "Then re-run: make install" >&2; \
		echo "If that fails, ensure you have build tools: https://visualstudio.microsoft.com/visual-cpp-build-tools/" >&2; \
		exit 1; \
	)
	cd frontend && npm install
	@echo "✅ Installation complete"

setup: install
	@echo "Setting up project..."
	git init || true
	pre-commit install || true
	cd backend && alembic upgrade head || true
	@echo "✅ Project setup complete"

# Development
dev:
	@echo "Starting services with Docker Compose..."
	docker-compose up

dev-local:
	@echo "Starting services locally..."
	$(MAKE) -j2 dev-backend dev-frontend

dev-backend:
	cd backend && uv run uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload

dev-frontend:
	cd frontend && npm run dev

# Testing
test: test-unit test-integration
	@echo "✅ All tests passed"

test-unit:
	@echo "Running unit tests..."
	cd backend && uv run pytest tests/unit -v --cov=app

test-integration:
	@echo "Running integration tests..."
	cd backend && uv run pytest tests/integration -v --cov=app

test-e2e:
	@echo "Running E2E tests..."
	npx playwright test tests_e2e/

test-coverage:
	@echo "Generating coverage report..."
	cd backend && uv run pytest tests/ --html=htmlcov/index.html --self-contained-html
	@echo "📊 Coverage report: htmlcov/index.html"

# Code Quality
lint:
	@echo "Running linting..."
	cd backend && uv run ruff check .

format:
	@echo "Formatting code..."
	cd backend && uv run ruff format .

type-check:
	@echo "Running type checks..."
	cd backend && uv run mypy app/

quality: lint type-check
	@echo "✅ Code quality checks passed"

# Database
migrate:
	@echo "Running database migrations..."
	cd backend && uv run alembic upgrade head

migrate-create:
	@echo "Creating new migration..."
	@read -p "Migration name: " name; \
	cd backend && uv run alembic revision --autogenerate -m "$$name"

seed:
	@echo "Seeding database..."
	cd backend && uv run python -c "from app.database.seed import seed_data; seed_data()"

# Docker
build:
	@echo "Building Docker images..."
	docker-compose build

build-backend:
	@echo "Building backend image..."
	docker build -t {{ cookiecutter.project_slug }}-backend:latest ./backend

build-frontend:
	@echo "Building frontend image..."
	docker build -t {{ cookiecutter.project_slug }}-frontend:latest ./frontend

# Cleanup
clean:
	@echo "Cleaning build artifacts..."
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".pytest_cache" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".mypy_cache" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".ruff_cache" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name "*.egg-info" -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name ".coverage" -delete 2>/dev/null || true
	@echo "✅ Clean complete"

clean-docker:
	@echo "Removing Docker containers and volumes..."
	docker-compose down -v
	docker system prune -f
	@echo "✅ Docker cleanup complete"

clean-cache:
	@echo "Clearing uv package cache..."
	uv cache clean
	@echo "✅ Cache cleaned"

clean-all: clean clean-docker
	@echo "Removing virtual environments..."
	rm -rf backend/.venv frontend/node_modules
	@echo "✅ Full cleanup complete"

# CI/CD
ci: lint type-check test
	@echo "✅ CI checks passed"

# Shortcuts
b: build
d: dev
t: test
l: lint
f: format
c: clean
m: migrate

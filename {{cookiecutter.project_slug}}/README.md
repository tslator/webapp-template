# {{ cookiecutter.project_name }}

{{ cookiecutter.project_description }}

## Features

- **FastAPI Backend** - Modern async Python web framework
- **SQLAlchemy ORM** - Type-safe database models
- **HTMX Frontend** - Lightweight interactivity without heavy JavaScript
- **Tailwind CSS** - Utility-first styling framework
- **Docker Support** - Containerized development and deployment
- **Pre-commit Hooks** - Automated code quality checks
- **Comprehensive Tests** - Unit, integration, and E2E testing
- **GitHub Actions CI/CD** - Automated testing and deployment
- **Alembic Migrations** - Database versioning and schema management

## Quick Start

### Prerequisites
- Python {{ cookiecutter.python_version }}
- Docker and Docker Compose (optional)
- Node.js 20+ (for frontend development)

### Setup with Docker Compose

```bash
# Clone and navigate to project
cd {{ cookiecutter.project_slug }}

# Start all services
make dev

# Access the application
# Backend API: http://localhost:8000
# API Documentation: http://localhost:8000/docs
# Frontend: http://localhost:3000
```

### Local Development Setup

```bash
# Install dependencies
make install

# Run migrations
make migrate

# Start backend and frontend
make dev-local

# In a new terminal, run tests
make test
```

## Project Structure

```
.
├── backend/                    # FastAPI application
│   ├── app/
│   │   ├── main.py            # Application factory
│   │   ├── config.py          # Configuration
│   │   ├── api/               # API routes and schemas
│   │   ├── models/            # Database models
│   │   ├── database/          # Database configuration
│   │   └── tests/             # Unit and integration tests
│   ├── migrations/            # Alembic database migrations
│   ├── Dockerfile             # Backend container
│   └── pyproject.toml         # Dependencies
├── frontend/                  # HTML/HTMX/Tailwind frontend
│   ├── templates/             # HTML templates
│   ├── static/                # CSS, JavaScript, images
│   ├── Dockerfile             # Frontend container
│   ├── package.json           # Node dependencies
│   └── tailwind.config.js     # Tailwind configuration
├── tests_e2e/                 # End-to-end tests
├── docker-compose.yml         # Multi-container orchestration
├── Makefile                   # Development commands
└── .github/                   # GitHub Actions workflows
```

## Common Commands

### Development
```bash
make dev              # Run with Docker Compose
make dev-local        # Run locally without Docker
```

### Testing
```bash
make test             # Run all tests
make test-unit        # Run unit tests
make test-integration # Run integration tests
make test-e2e         # Run end-to-end tests
make test-coverage    # Generate coverage report
```

### Code Quality
```bash
make lint             # Run linting
make format           # Format code
make type-check       # Run type checking
make quality          # Run all quality checks
```

### Database
```bash
make migrate          # Run migrations
make migrate-create   # Create new migration
make seed             # Populate with sample data
```

### Docker
```bash
make build            # Build Docker images
make clean-docker     # Clean Docker containers
```

## Environment Variables

See `backend/.env.example` for all available configuration options.

```bash
# Copy the example
cp backend/.env.example backend/.env

# Edit with your settings
nano backend/.env
```

## API Documentation

Once the application is running, visit `http://localhost:8000/docs` for interactive API documentation.

## Testing

The project includes:
- **Unit Tests**: Fast, isolated business logic tests
- **Integration Tests**: API and database integration tests
- **E2E Tests**: Full user workflow tests with Playwright

```bash
# Run all tests with coverage
make test

# Generate HTML coverage report
make test-coverage
```

## Deployment

### Docker

```bash
# Build images
make build

# Push to registry
docker tag {{ cookiecutter.project_slug }}:latest your-registry/{{ cookiecutter.project_slug }}:latest
docker push your-registry/{{ cookiecutter.project_slug }}:latest
```

### Production Environment

Update environment variables for production:
```bash
DEBUG=False
PYTHONUNBUFFERED=1
DATABASE_URL=postgresql+asyncpg://...
JWT_SECRET_KEY=your-production-secret
CORS_ORIGINS=["https://yourdomain.com"]
```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

Code quality checks run automatically via pre-commit hooks and CI/CD pipelines.

## License

This project is licensed under the {{ cookiecutter.license }} License - see LICENSE file for details.

## Support

For issues and feature requests, please open an issue on GitHub.

## Author

{{ cookiecutter.full_name }} ({{ cookiecutter.email }})

Created with the [Python Web App Template](https://github.com/{{ cookiecutter.github_username }}/webapp-template)

"""Health check and User API routes."""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.schemas.user import UserCreate, UserResponse
from app.database.session import get_session
from app.models.user import User

# Routers
health_router = APIRouter(tags=["health"])
user_router = APIRouter(prefix="/users", tags=["users"])


@health_router.get("/")
async def root():
    """Root endpoint."""
    return {"message": "Welcome to {{ cookiecutter.project_name }} API"}


@user_router.post("/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def create_user(
    user_create: UserCreate,
    session: AsyncSession = Depends(get_session),
):
    """Create a new user."""
    # Check if user already exists
    existing_user = await session.query(User).filter(
        (User.email == user_create.email) | (User.username == user_create.username)
    ).first()

    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with this email or username already exists",
        )

    # Create new user
    new_user = User(
        username=user_create.username,
        email=user_create.email,
        full_name=user_create.full_name,
        hashed_password=user_create.password,  # In production, hash the password!
    )

    session.add(new_user)
    await session.commit()
    await session.refresh(new_user)

    return new_user


@user_router.get("/", response_model=list[UserResponse])
async def list_users(
    skip: int = 0,
    limit: int = 100,
    session: AsyncSession = Depends(get_session),
):
    """List all users."""
    users = await session.query(User).offset(skip).limit(limit).all()
    return users


@user_router.get("/{user_id}", response_model=UserResponse)
async def get_user(
    user_id: int,
    session: AsyncSession = Depends(get_session),
):
    """Get a specific user by ID."""
    user = await session.query(User).filter(User.id == user_id).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )

    return user


@user_router.put("/{user_id}", response_model=UserResponse)
async def update_user(
    user_id: int,
    user_update: dict,
    session: AsyncSession = Depends(get_session),
):
    """Update a user."""
    user = await session.query(User).filter(User.id == user_id).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )

    for key, value in user_update.items():
        if value is not None:
            setattr(user, key, value)

    await session.commit()
    await session.refresh(user)

    return user


@user_router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(
    user_id: int,
    session: AsyncSession = Depends(get_session),
):
    """Delete a user."""
    user = await session.query(User).filter(User.id == user_id).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )

    await session.delete(user)
    await session.commit()

    return None

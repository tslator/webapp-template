"""Example unit tests."""

import pytest

from app.models.user import User


@pytest.mark.asyncio
async def test_create_user():
    """Test user creation."""
    user = User(
        username="testuser",
        email="test@example.com",
        full_name="Test User",
        hashed_password="hashedpass123",
    )

    assert user.username == "testuser"
    assert user.email == "test@example.com"
    assert user.is_active is True
    assert user.is_superuser is False


@pytest.mark.asyncio
async def test_user_repr():
    """Test user string representation."""
    user = User(
        id=1,
        username="testuser",
        email="test@example.com",
        full_name="Test User",
        hashed_password="hashedpass123",
    )

    assert "testuser" in repr(user)
    assert "User" in repr(user)

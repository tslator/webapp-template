#!/usr/bin/env python
"""Seed database with sample data."""

import asyncio
from app.database.session import async_session_maker
from app.models.user import User


async def seed_data():
    """Populate database with sample data."""
    async with async_session_maker() as session:
        # Check if data already exists
        existing = await session.query(User).first()
        if existing:
            print("Database already seeded")
            return

        # Create sample users
        users = [
            User(
                username="admin",
                email="admin@example.com",
                full_name="Admin User",
                hashed_password="admin123",
                is_superuser=True,
                is_active=True,
            ),
            User(
                username="user1",
                email="user1@example.com",
                full_name="User One",
                hashed_password="password123",
                is_active=True,
            ),
            User(
                username="user2",
                email="user2@example.com",
                full_name="User Two",
                hashed_password="password123",
                is_active=True,
            ),
        ]

        for user in users:
            session.add(user)

        await session.commit()
        print(f"Seeded {len(users)} users")


if __name__ == "__main__":
    asyncio.run(seed_data())

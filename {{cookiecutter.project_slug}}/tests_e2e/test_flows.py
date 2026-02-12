"""Example E2E tests with Playwright."""

import pytest


@pytest.mark.asyncio
async def test_homepage_loads(browser):
    """Test that homepage loads."""
    page = await browser.new_page()
    await page.goto("http://localhost:3000")

    # Check page title
    title = await page.title()
    assert "{{ cookiecutter.project_name }}" in title

    # Check main heading
    heading = await page.query_selector("h1")
    assert heading is not None

    await page.close()


@pytest.mark.asyncio
async def test_api_docs_available(browser):
    """Test that API docs are available."""
    page = await browser.new_page()
    await page.goto("http://localhost:8000/docs")

    # Check for Swagger UI
    await page.wait_for_load_state("networkidle")
    content = await page.content()
    assert "swagger" in content.lower() or "openapi" in content.lower()

    await page.close()

# import pytest
# from httpx import AsyncClient
# from src.main import app  # Import FastAPI app
#
# @pytest.fixture
# async def test_client():
#     async with AsyncClient(app=app, base_url="http://test") as client:
#         yield client
#


# import pytest
# import pytest_asyncio
# from httpx import AsyncClient
# from fastapi.testclient import TestClient
# from src.main import app  # Ensure FastAPI app is correctly imported
#
# # Create a synchronous test client for startup
# test_client = TestClient(app)
#
# @pytest_asyncio.fixture
# async def async_test_client():
#     """Fixture to provide an asynchronous HTTP test client."""
#     async with AsyncClient(base_url="http://test", transport=test_client.transport) as ac:
#         yield ac  # Correctly yield async client
#
# import pytest
# import pytest_asyncio
# from httpx import AsyncClient
# from src.main import app
# from fastapi.testclient import TestClient
#
# # Create a FastAPI test instance
# @pytest_asyncio.fixture
# async def async_test_client():
#     """Fixture to provide an asynchronous HTTP test client."""
#     client = TestClient(app)  # Create FastAPI test client
#     async with AsyncClient(base_url="http://test", transport=client.transport, follow_redirects=True) as ac:
#         yield ac  # Correctly yield async client


import pytest
import pytest_asyncio
from httpx import AsyncClient
from fastapi.testclient import TestClient
from httpx import ASGITransport  # ✅ Correct transport for FastAPI apps
from src.main import app

import asyncio
#
# @pytest.fixture(scope="session")
# def event_loop():
#     loop = asyncio.new_event_loop()
#     yield loop
#     loop.close()

pytest_plugins = "pytest_asyncio"

def pytest_configure(config):
    config.option.asyncio_mode = "auto"

@pytest.fixture(scope="session")
def event_loop():
    """Ensure tests run on the same event loop."""
    loop = asyncio.get_event_loop()
    yield loop
    loop.close()


@pytest_asyncio.fixture
async def async_test_client():
    """Fixture to provide an asynchronous HTTP test client."""
    async with AsyncClient(transport=ASGITransport(app), base_url="http://test", follow_redirects=True) as ac:
        yield ac  # Correctly yield async client
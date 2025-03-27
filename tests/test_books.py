import pytest

@pytest.mark.asyncio
async def test_add_book(async_test_client):
    book_data = {
            "title": "Sample Book",
            "author": "Author",
            "genre": "Fiction",
            "year_published": 2024,
            "summary": "test summary content"

    }
    response = await async_test_client.post("/books/", json=book_data)
    print(response.json())
    assert response.status_code == 201

@pytest.mark.asyncio
async def test_get_books(async_test_client):
    response = await async_test_client.get("/books/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

import pytest

@pytest.mark.asyncio
async def test_add_review(async_test_client):
    # First, create a book
    book_data = {
                "title": "Sample Book",
                "author": "Author",
                "genre": "Fiction",
                "year_published": 2024,
                "summary": "test summary content"
        }
    book_response = await async_test_client.post("/books/", json=book_data)
    book_id = book_response.json()["id"]

    # Now, add a review
    review_response = await async_test_client.post(f"/books/{book_id}/reviews", json={
        "user_id": 1,
        "review_text": "Amazing book!",
        "rating": 4.5
    })
    assert review_response.status_code == 201
    assert review_response.json()["review_text"] == "Amazing book!"



@pytest.mark.asyncio
async def test_get_reviews(async_test_client):
    response = await async_test_client.get("/books/1/reviews")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

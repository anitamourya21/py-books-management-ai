import pytest

@pytest.mark.asyncio
async def test_generate_book_summary(async_test_client):
    response = await async_test_client.post("/generate-summary/1", json={
        "title": "AI Book",
        "content": "This is an AI-generated book summary test."
    })
    assert response.status_code == 200
    assert "summary" in response.json()
#
# @pytest.mark.asyncio
# async def test_get_book_recommendations(async_test_client):
#     response = await async_test_client.get("/recommendations?genre=Fiction")
#     assert response.status_code == 200
#     assert isinstance(response.json(), list)
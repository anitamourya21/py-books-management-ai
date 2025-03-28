from src.repositories import BookRepository, ReviewRepository
from src.models import Book, Review
from src.ai_service import AIService
from fastapi import Depends, Response

class BookService:
    def __init__(self, book_repo: BookRepository):
        self.book_repo = book_repo

    async def add_book(self, book_data):
        return await self.book_repo.add_book(book_data)

    async def update_book(self, book_id: int, book_data):
        return await self.book_repo.update_book(book_id, book_data)

    async def get_books(self):
        return await self.book_repo.get_books()

    async def get_book_by_id(self, book_id: int):
        return await self.book_repo.get_book_by_id(book_id)

class ReviewService:
    def __init__(self, review_repo: ReviewRepository):
        self.review_repo = review_repo

    async def add_review(self, book_id, review_data):
        return await self.review_repo.add_review(book_id, review_data)

    async def get_reviews_for_book(self, book_id: int):
        return await self.review_repo.get_reviews_by_book(book_id)


class SummaryService:
    def __init__(self, bservice: BookService):
        self.bservice = bservice
        self.service = AIService()


    async def get_summary_for_book(self, book_id: int):
        book_data = await self.bservice.get_book_by_id(book_id)
        title = book_data.title
        content = book_data.summary

        summary_ai = await self.service.generate_summary(title, content)
        if summary_ai:
            book_data = {}
            book_data["summary_ai"] = summary_ai
            await self.bservice.update_book(book_id, book_data)

        return summary_ai


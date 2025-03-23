from src.repositories import BookRepository, ReviewRepository
from src.models import Book, Review

class BookService:
    def __init__(self, book_repo: BookRepository):
        self.book_repo = book_repo

    async def add_book(self, book_data):
#         book = Book(**book_data.dict())
        return await self.book_repo.add_book(book_data)

    async def get_books(self):
        return await self.book_repo.get_books()

    async def get_book_by_id(self, book_id: int):
        return await self.book_repo.get_book_by_id(book_id)

class ReviewService:
    def __init__(self, review_repo: ReviewRepository):
        self.review_repo = review_repo

    async def add_review(self, book_id, review_data):
#         review = Review(**review_data)
        return await self.review_repo.add_review(book_id, review_data)

    async def get_reviews_for_book(self, book_id: int):
        return await self.review_repo.get_reviews_by_book(book_id)
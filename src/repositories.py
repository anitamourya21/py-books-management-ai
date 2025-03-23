from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from src.models import Book, Review
from src.schemas import BookCreate, ReviewCreate
from traceback import print_exception

class BookRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def add_book(self, book_data: BookCreate):
        try:
            if not isinstance(book_data, BookCreate):  # Ensure it's a Pydantic model
              raise TypeError("book_data must be a Pydantic model")

            book = Book(**book_data.dict())
            self.session.add(book)
            await self.session.commit()
            await self.session.refresh(book)
            return book
        except Exception:
            print_exception(e)
            return Response("Internal server error", status_code=500)

    async def get_books(self):
        try:
            result = await self.session.execute(select(Book))
            return result.scalars().all()
        except Exception as e:
            print_exception(e)
            raise e

    async def get_book_by_id(self, book_id: int):
        return await self.session.get(Book, book_id)

class ReviewRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def add_review(self, book_id: int, review_data: ReviewCreate):
        try:
            if not isinstance(review_data, ReviewCreate):  # Ensure it's a Pydantic model
               raise TypeError("review_data must be a Pydantic model")
            review_dict = review_data.dict()
            review_dict["book_id"] = book_id
            review = Review(**review_dict)
            self.session.add(review)
            await self.session.commit()
            return review
        except Exception:
            print_exception(e)
            return Response("Internal server error", status_code=500)

    async def get_reviews_by_book(self, book_id: int):
        result = await self.session.execute(select(Review).filter(Review.book_id == book_id))
        return result.scalars().all()
from fastapi import FastAPI, Depends, Response
from sqlalchemy.ext.asyncio import AsyncSession
from src.database import get_db
from src.services import BookService, ReviewService, SummaryService
from src.repositories import BookRepository, ReviewRepository
from src.schemas import BookCreate, BookResponse, ReviewCreate, ReviewResponse
from typing import List

app = FastAPI()

# Dependency injection
async def get_book_service(db: AsyncSession = Depends(get_db)):
    return BookService(BookRepository(db))

async def get_summary_service(bservice: BookService = Depends(get_book_service)):
    return SummaryService(bservice)

async def get_review_service(db: AsyncSession = Depends(get_db)):
    return ReviewService(ReviewRepository(db))

@app.post("/books/", response_model=BookResponse)
async def add_book(book_data: BookCreate, service: BookService = Depends(get_book_service)):
    return await service.add_book(book_data)

@app.get("/books/", response_model=List[BookResponse])
async def get_books(service: BookService = Depends(get_book_service)):
    try:
        return await service.get_books()
    except Exception as e:
        return Response("Some error occurred", 500)

@app.get("/books/{book_id}", response_model=BookResponse)
async def get_book(book_id: int, service: BookService = Depends(get_book_service)):
    return await service.get_book_by_id(book_id)

@app.post("/books/{book_id}/reviews/", response_model=ReviewResponse)
async def add_review(book_id: int, review_data: ReviewCreate, service: ReviewService = Depends(get_review_service)):
#     review_data.book_id = book_id
    return await service.add_review(book_id, review_data)

@app.get("/books/{book_id}/reviews/", response_model=List[ReviewResponse])
async def get_reviews(book_id: int, service: ReviewService = Depends(get_review_service)):
    return await service.get_reviews_for_book(book_id)

#
@app.post("/generate-summary/{book_id}")
async def generate_summary(book_id: int, service: SummaryService = Depends(get_summary_service)):
    summary = await service.get_summary_for_book(book_id)
    return {"summary": summary}

@app.get("/check-summary")
async def check_summary(service: SummaryService = Depends(get_summary_service)):
    summary = await service.check_summary_for_book()
    return {"summary": summary}
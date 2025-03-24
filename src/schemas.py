from pydantic import BaseModel, Field
from typing import List, Optional

# Book Schema
class BookCreate(BaseModel):
    title: str = Field(..., example="The Great Gatsby")
    author: str = Field(..., example="F. Scott Fitzgerald")
    genre: Optional[str] = Field(..., example="Fiction")
    year_published: Optional[int] = Field(..., example=1925)
    summary: Optional[str] = Field(..., example="The Great Gatsby, by F. Scott Fitzgerald, is an epic adventure that takes readers through glittering nights and fading sunsets of a decadent era.")

class BookResponse(BookCreate):
    id: int

    class Config:
        from_attributes = True

# Review Schema
class ReviewCreate(BaseModel):
    user_id: int = Field(..., example=123)
    review_text: str = Field(..., example="Amazing book!")
    rating: float = Field(..., ge=0, le=5, example=4.5)

class ReviewResponse(ReviewCreate):
    id: int
    book_id: int

    class Config:
        from_attributes = True
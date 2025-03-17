from pydantic import BaseModel
from typing import Optional

# Schema for adding a new book
class BookCreate(BaseModel):
    title: str
    author: str
    category: str
    price: float
    description: str


# Schema for updating an existing book
class BookUpdate(BaseModel):
    title: Optional[str] = None
    author: Optional[str] = None
    category: Optional[str] = None
    price: Optional[float] = None
    description: Optional[str] = None


# Schema for response (includes ID)
class BookResponse(BookCreate):
    id: int

    class Config:
        from_attributes = True  # Allows ORM models to be converted to Pydantic models
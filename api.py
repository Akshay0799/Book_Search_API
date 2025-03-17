from fastapi import FastAPI, HTTPException, Depends, Query
# from config import settings
from sqlalchemy.orm import Session
import models, schema, database
from ml_utils import SemanticSearch
from typing import Optional

app = FastAPI()

models.Base.metadata.create_all(bind=database.engine)

# Dependency to get the database session
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_hello():
    return {"message": "Hello, World!"}


# Add a book to the repository
@app.post("/books/", response_model=schema.BookResponse)
def create_book(book: schema.BookCreate, db: Session = Depends(get_db)):
    db_book = models.Book(**book.dict())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

# Get All Books (with optional filtering)
@app.get("/books/", response_model=list[schema.BookResponse])
def get_books(
    db: Session = Depends(get_db)
):
    query = db.query(models.Book)
    return query.all()

# Get a Book by ID
@app.get("/books/{id}", response_model=schema.BookResponse)
def get_Book(id: int, db: Session = Depends(get_db)):
    book = db.query(models.Book).filter(models.Book.id == id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

# Update a Book
@app.put("/books/{id}")
def update_Book(id: int, book: schema.BookUpdate, db: Session = Depends(get_db)):
    db_book = db.query(models.Book).filter(models.Book.id == id).first()
    if not db_book:
        raise HTTPException(status_code=404, detail="Book not found")

    update_data = book.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_book, key, value)

    db.commit()
    return {"message": "Book updated successfully"}

# Delete a Book
@app.delete("/books/{id}")
def delete_book(id: int, db: Session = Depends(get_db)):
    book = db.query(models.Book).filter(models.Book.id == id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")

    db.delete(book)
    db.commit()
    return {"message": "Book deleted successfully"}

# Semantic Search for recommendations based on Title
@app.get("/books/search/{title}")
def search_book(title: str, db: Session = Depends(get_db)):
    query = db.query(models.Book).all()
    searchObj = SemanticSearch(query)
    results = searchObj.search_title(title)
    return results

# Filter books based on Category or prices
@app.get("/books/filter/", response_model=list[schema.BookResponse])
def filter_book(title: Optional[str] = Query(None), category: Optional[str] = Query(None), min_price: Optional[float] = Query(None), author: Optional[str] = Query(None), db: Session = Depends(get_db)):
    query = db.query(models.Book)

    if title:
        query = query.filter(models.Book.title == title)
    if category:
        query = query.filter(models.Book.title == category)
    if author:
        query = query.filter(models.Book.author == author)
    if min_price:
        query = query.filter(models.Book.price >= min_price)
    
    return query.all()

# Recommendation of books based on description
@app.get("/books/recommend/{id}", response_model=list[schema.BookResponse])
def recommend_books(id: int, db: Session = Depends(get_db)):
    book = db.query(models.Book).filter(models.Book.id == id).first()
    books = db.query(models.Book).all()
    searchObj = SemanticSearch(books)
    results = searchObj.recommend(book)
    return results





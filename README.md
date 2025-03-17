# Book_Search_API
An API hosting a book inventory that enables users to search for books and get recommendations


## Technologies
* FastAPI (Backend)
* SQLite / PostgreSQL (Database)
* Sentence Transformers (For semantic search)
* SQLAlchemy (ORM for database interaction)
* Uvicorn (ASGI server for FastAPI)

## Functionalities

* CRUD operations for managing Books (Add, Retrieve, Update, Delete)
* Filter books by title,category, author, minimum price
* Semantic search for Books based on User Input
* Book recommendations based on similar descriptions
* FastAPI backend with SQLite/PostgreSQL for storage

## Instructions to run the code
* Install dependencies
  ```
  pip install -r requirements.txt
  ```
* Start the FastAPI Server
  ```
  uvicorn api:app --reload
  ```
* Test the API endpoints
  ```
  python test_api.py
  ```

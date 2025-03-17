sample_books = [
    {
        "title": "The Silent Patient",
        "author": "Alex Michaelides",
        "category": "Thriller",
        "price": 12.99,
        "description": "A psychological thriller about a woman who stops speaking after committing a violent crime."
    },
    {
        "title": "Atomic Habits",
        "author": "James Clear",
        "category": "Self-Help",
        "price": 16.50,
        "description": "A book about building good habits and breaking bad ones through small changes."
    },
    {
        "title": "Dune",
        "author": "Frank Herbert",
        "category": "Science Fiction",
        "price": 14.99,
        "description": "A sci-fi epic set in a desert world filled with intrigue, politics, and adventure."
    },
    {
        "title": "Educated",
        "author": "Tara Westover",
        "category": "Memoir",
        "price": 18.99,
        "description": "A memoir of a woman who escapes her survivalist family and earns a PhD from Cambridge."
    },
    {
        "title": "The Alchemist",
        "author": "Paulo Coelho",
        "category": "Fiction",
        "price": 11.99,
        "description": "A novel about a shepherd's journey to discover his personal legend and fulfill his dreams."
    },
    {
        "title": "Deep Learning",
        "author": "Ian Goodfellow, Yoshua Bengio, Aaron Courville",
        "category": "Technology",
        "price": 52.99,
        "description": "A comprehensive textbook covering the fundamentals of deep learning."
    },
    {
        "title": "The Hobbit",
        "author": "J.R.R. Tolkien",
        "category": "Fantasy",
        "price": 10.99,
        "description": "A classic fantasy adventure following Bilbo Baggins on his quest to reclaim a lost treasure."
    },
    {
        "title": "Sapiens: A Brief History of Humankind",
        "author": "Yuval Noah Harari",
        "category": "History",
        "price": 19.99,
        "description": "A book exploring the history and impact of Homo sapiens on the world."
    },
    {
        "title": "The Subtle Art of Not Giving a F*ck",
        "author": "Mark Manson",
        "category": "Self-Help",
        "price": 15.75,
        "description": "A book that challenges traditional self-help advice and advocates for a more practical approach to happiness."
    },
    {
        "title": "Machine Learning Yearning",
        "author": "Andrew Ng",
        "category": "Technology",
        "price": 29.99,
        "description": "A guide for machine learning practitioners on how to build and improve AI models."
    }
]

import requests

BASE_URL = "http://127.0.0.1:8000"  # Update if your API runs on a different port

# Sample book data
# sample_book = {
#     "title": "The AI Revolution",
#     "author": "John Doe",
#     "category": "Technology",
#     "price": 39.99
# }

# 1️⃣ Create a book entries
def test_create_books():
    print("\n📌 Creating new books...")
    for book in sample_books:
        response = requests.post(f"{BASE_URL}/books/", json=book)
        print(response.status_code, response.json())
    

# 2️⃣ Get all books
def test_get_books():
    print("\n📌 Fetching all books...")
    response = requests.get(f"{BASE_URL}/books/")
    print(response.status_code, response.json())

# 3️⃣ Get a book by ID
def test_get_book_by_id(book_id=1):
    print(f"\n📌 Fetching book with ID {book_id}...")
    response = requests.get(f"{BASE_URL}/books/{book_id}")
    print(response.status_code, response.json())

# 4️⃣ Update a book
def test_update_book(book_id=1):
    updated_data = {"title": "Updated AI Book", "price": 45.99}
    print(f"\n📌 Updating book with ID {book_id}...")
    response = requests.put(f"{BASE_URL}/books/{book_id}", json=updated_data)
    print(response.status_code, response.json())

# 5️⃣ Delete a book
def test_delete_book(book_id=1):
    print(f"\n📌 Deleting book with ID {book_id}...")
    response = requests.delete(f"{BASE_URL}/books/{book_id}")
    print(response.status_code, response.json())

# 6️⃣ Test Semantic Search
def test_semantic_search(query="Deep Learning Concepts"):
    print(f"\n📌 Performing semantic search for '{query}'...")
    response = requests.get(f"{BASE_URL}/books/search/{query}")
    print(response.status_code, response.json())

# Test Recommendation
def test_recommendation(id=5):
    print(f"\n📌 Fetching recommendation for book '{id}'... - Deep Learning Concepts")
    response = requests.get(f"{BASE_URL}/books/recommend/{id}")
    print(response.status_code, response.json())

def test_filter_book_by_author(author = "Andrew Ng"):
    params = {
        "author": author
    }
    print(f"\n📌 Fetching book with author name {author}...")
    response = requests.get(f"{BASE_URL}/books/filter/", params=params)
    print(response.status_code, response.json())


# # 🚀 Run Tests
# if __name__ == "__main__":
#     test_create_books()
#     test_get_books()
#     test_get_book_by_id()
#     test_update_book()
#     test_get_books()  # Check updates
#     test_semantic_search()
#     test_delete_book()
#     test_recommendation()
#     test_filter_book_by_author()
#     test_get_books()  # Verify deletion
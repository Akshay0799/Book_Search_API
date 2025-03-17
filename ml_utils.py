import torch
from sentence_transformers import SentenceTransformer, util
import pandas as pd
import pickle
from sklearn.decomposition import PCA
from umap import UMAP
import numpy as np

class SemanticSearch:
    def __init__(self, books: list,) -> None:
        self.books = books
        self.bookTitles = [book.title for book in books]
        self.bookDesc = [book.description for book in books]

        self.model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

        # with open('meme-embeddings.pkl', "wb") as fOut:
        #     pickle.dump(reduced_embeddings, fOut)
    
    def search(self, userQuery: str):
        try:
            book_embedding = self.model.encode([userQuery])

            # self.bookTitles.remove(bookTitle)

            # Use PCA for dimensionality reduction
            embeddings = self.model.encode(self.bookTitles, show_progress_bar=True)
            pca = PCA(n_components = 2)
            reduced_embeddings = pca.fit_transform(embeddings)
            reduced_book_embeddings = pca.transform(book_embedding)
            hits = util.semantic_search(reduced_book_embeddings, reduced_embeddings, top_k=2) 
            print(f"Results of semantic search:{hits}")
            return [self.books[hits[0][0]['corpus_id']], self.books[hits[0][1]['corpus_id']]]
        except Exception as e:
            print(f"Error while searching:{e}")
    
    def recommend(self, book):
        try:

            search_desc = book.description
            # print("input desc:",search_desc)
            book_embedding = self.model.encode([search_desc])
            
            # self.bookDesc.remove(search_desc)
            # print("search space desc:",self.bookDesc)
            # Uses UMAP for dimensionality reduction
            
            embeddings = self.model.encode(self.bookDesc, show_progress_bar=True)


            umap = UMAP(n_components=3, n_neighbors = 8)
            reduced_embeddings = umap.fit_transform(embeddings)
            reduced_book_embedding = umap.transform(book_embedding)

            # # Normalization
            # reduced_book_embedding = reduced_book_embedding / np.linalg.norm(reduced_book_embedding, axis=1, keepdims=True)
            # reduced_embeddings = reduced_embeddings/ np.linalg.norm(reduced_embeddings, axis=1, keepdims=True)
            
            # Convert to PyTorch tensor
            reduced_embeddings = torch.tensor(reduced_embeddings)  
            reduced_book_embedding = torch.tensor(reduced_book_embedding)

            # Normalization
            normalized_embeddings = util.normalize_embeddings(reduced_embeddings)
            normalized_book_embedding = util.normalize_embeddings(reduced_book_embedding)

            hits = util.semantic_search(normalized_book_embedding, normalized_embeddings, top_k=2) 

            print(f"Results of semantic search:{hits}")
            return [self.books[hits[0][0]['corpus_id']], self.books[hits[0][1]['corpus_id']]]
                
        except Exception as e:
            print(f"Error while recommending:{e}")

if __name__ == "__main__":
    books = [

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
        "description": "A self help book about building good habits and breaking bad ones through small changes."
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
        "description": "A comprehensive textbook covering the fundamentals of deep learning, machine learning and AI models."
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
    searchObj = SemanticSearch(books, desc=True)
    results = searchObj.recommend(books[5])
    print(results)
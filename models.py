from database import Base
from sqlalchemy import Column, Integer, String, Float

class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    author = Column(String)
    category = Column(String)
    price = Column(Float)
    description = Column(String)
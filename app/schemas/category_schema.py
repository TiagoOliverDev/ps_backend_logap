# app/schemas/category_schema.py
from pydantic import BaseModel
from typing import List, Optional
from app.schemas.product_schema import Product

class CategoryBase(BaseModel):
    name: str

class CategoryCreate(CategoryBase):
    pass

class Category(CategoryBase):
    id: int
    products: Optional[List[Product]] = None  # Inclui produtos de maneira opcional.

    class Config:
        from_attributes = True

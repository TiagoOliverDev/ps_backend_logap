from typing import List
from pydantic import BaseModel

class ProductBase(BaseModel):
    name: str
    purchase_price: float
    quantity: int
    sale_price: float
    category_id: int
    supplier_id: int

class ProductCreate(ProductBase):
    pass

class Product(ProductBase):
    id: int

    class Config:
        from_attributes = True

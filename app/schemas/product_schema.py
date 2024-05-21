# app/schemas/product_schema.py
from pydantic import BaseModel

class ProductBase(BaseModel):
    name: str
    purchase_price: float
    quantity: int
    sale_price: float

class ProductCreate(ProductBase):
    category_id: int
    supplier_id: int

class Product(ProductBase):
    id: int
    category_id: int
    supplier_id: int

    class Config:
        from_attributes = True

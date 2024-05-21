# app/services/product_service.py
from sqlalchemy.orm import Session
from typing import List
from app.schemas.product_schema import ProductCreate, Product
from app.repositories.product_repository import ProductRepository

class ProductService:
    def __init__(self, db: Session):
        self.db = db
        self.product_repo = ProductRepository(db)

    def create_product(self, product: ProductCreate) -> Product:
        return self.product_repo.create(product)

    def get_products(self, skip: int = 0, limit: int = 10) -> List[Product]:
        return self.product_repo.get_all(skip=skip, limit=limit)

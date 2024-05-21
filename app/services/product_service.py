# app/services/product_service.py
from sqlalchemy.orm import Session
from app.schemas.product_schema import ProductCreate, Product
from app.repositories.product_repository import ProductRepository

class ProductService:
    def __init__(self, db: Session):
        self.repository = ProductRepository(db)

    def create_product(self, product_data: ProductCreate) -> Product:
        return self.repository.create(product_data)

    def get_product(self, product_id: int) -> Product:
        return self.repository.get_by_id(product_id)

    def get_products(self, skip: int = 0, limit: int = 10) -> list:
        return self.repository.get_all(skip, limit)

    def update_product(self, product_id: int, product_data: ProductCreate) -> Product:
        return self.repository.update(product_id, product_data)

    def delete_product(self, product_id: int) -> bool:
        return self.repository.delete(product_id)

# app/repositories/product_repository.py
from sqlalchemy.orm import Session
from app.models.models import Product
from app.schemas.product_schema import ProductCreate

class ProductRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, product_data: ProductCreate):
        product = Product(**product_data.dict())
        self.db.add(product)
        self.db.commit()
        self.db.refresh(product)
        return product

    def get_by_id(self, product_id: int):
        return self.db.query(Product).filter(Product.id == product_id).first()

    def get_all(self, skip: int = 0, limit: int = 10):
        return self.db.query(Product).offset(skip).limit(limit).all()

    def update(self, product_id: int, product_data: ProductCreate):
        product = self.db.query(Product).filter(Product.id == product_id).first()
        if product:
            for var, value in product_data.dict().items():
                setattr(product, var, value)
            self.db.commit()
            self.db.refresh(product)
            return product
        return None

    def delete(self, product_id: int):
        product = self.db.query(Product).filter(Product.id == product_id).first()
        if product:
            self.db.delete(product)
            self.db.commit()
            return True
        return False

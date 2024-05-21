# app/repositories/product.py
from sqlalchemy.orm import Session
from app.models.models import Product
from app.schemas.product_schema import ProductCreate


class ProductRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, product: ProductCreate):
        db_product = Product(**product.dict())
        self.db.add(db_product)
        self.db.commit()
        self.db.refresh(db_product)
        return db_product

    def get(self, product_id: int):
        return self.db.query(Product).filter(Product.id == product_id).first()

    def get_all(self, skip: int = 0, limit: int = 10):
        return self.db.query(Product).offset(skip).limit(limit).all()

    def update(self, product_id: int, product: ProductCreate):
        db_product = self.db.query(Product).filter(Product.id == product_id).first()
        if db_product:
            for key, value in product.dict().items():
                setattr(db_product, key, value)
            self.db.commit()
            self.db.refresh(db_product)
        return db_product

    def delete(self, product_id: int):
        db_product = self.db.query(Product).filter(Product.id == product_id).first()
        if db_product:
            self.db.delete(db_product)
            self.db.commit()
        return db_product

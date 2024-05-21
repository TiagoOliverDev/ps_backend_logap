# app/repositories/category_repository.py
from sqlalchemy.orm import Session
from app.models.models import Category
from app.schemas.category_schema import CategoryCreate

class CategoryRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, category_data: CategoryCreate):
        category = Category(name=category_data.name)
        self.db.add(category)
        self.db.commit()
        self.db.refresh(category)
        return category

    def get_by_id(self, category_id: int):
        return self.db.query(Category).filter(Category.id == category_id).first()

    def get_all(self, skip: int = 0, limit: int = 10):
        return self.db.query(Category).offset(skip).limit(limit).all()

    def update(self, category_id: int, category_data: CategoryCreate):
        category = self.db.query(Category).filter(Category.id == category_id).first()
        if category:
            category.name = category_data.name
            self.db.commit()
            self.db.refresh(category)
            return category
        return None

    def delete(self, category_id: int):
        category = self.db.query(Category).filter(Category.id == category_id).first()
        if category:
            self.db.delete(category)
            self.db.commit()
            return True
        return False

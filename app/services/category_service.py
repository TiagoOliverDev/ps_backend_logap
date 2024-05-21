# app/services/category_service.py
from sqlalchemy.orm import Session
from app.schemas.category_schema import CategoryCreate, Category
from app.repositories.category_repository import CategoryRepository

class CategoryService:
    def __init__(self, db: Session):
        self.repository = CategoryRepository(db)

    def create_category(self, category_data: CategoryCreate) -> Category:
        return self.repository.create(category_data)

    def get_category(self, category_id: int) -> Category:
        return self.repository.get_by_id(category_id)
    
    def get_categories(self, skip: int = 0, limit: int = 10) -> list:
        return self.repository.get_all(skip, limit)

    def update_category(self, category_id: int, category_data: CategoryCreate) -> Category:
        return self.repository.update(category_id, category_data)

    def delete_category(self, category_id: int) -> bool:
        return self.repository.delete(category_id)

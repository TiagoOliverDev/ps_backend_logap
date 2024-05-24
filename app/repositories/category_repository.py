from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from app.models.models import Category
from app.schemas.category_schema import CategoryCreate

class CategoryRepository:
    def __init__(self, db: Session):
        """
        Initializes the CategoryRepository with a database session.

        Args:
            db (Session): The SQLAlchemy session for database interaction.
        """
        self.db = db

    def create(self, category_data: CategoryCreate) -> Category:
        """
        Creates a new category using the provided category data.

        Args:
            category_data (CategoryCreate): Data used to create a new category.

        Returns:
            Category: The newly created category instance.

        Raises:
            SQLAlchemyError: If a database operation fails.
        """
        try:
            category = Category(name=category_data.name)
            self.db.add(category)
            self.db.commit()
            self.db.refresh(category)
            return category
        except SQLAlchemyError as e:
            raise SQLAlchemyError(f"Failed to create category due to: {e}")

    def get_by_id(self, category_id: int) -> Category:
        """
        Retrieves a category by its ID.

        Args:
            category_id (int): The ID of the category to retrieve.

        Returns:
            Category: The retrieved category or None if not found.

        Raises:
            SQLAlchemyError: If a database operation fails.
        """
        try:
            return self.db.query(Category).filter(Category.id == category_id).first()
        except SQLAlchemyError as e:
            raise SQLAlchemyError(f"Failed to retrieve category due to: {e}")

    def get_all(self) -> list:
        """
        Retrieves all categories.

        Returns:
            list of Category: A list of categories.

        Raises:
            SQLAlchemyError: If a database operation fails.
        """
        try:
            return self.db.query(Category).all()
        except SQLAlchemyError as e:
            raise SQLAlchemyError(f"Failed to retrieve all categories due to: {e}")

    def update(self, category_id: int, category_data: CategoryCreate) -> Category:
        """
        Updates an existing category with the provided data.

        Args:
            category_id (int): The ID of the category to update.
            category_data (CategoryCreate): New data for the category.

        Returns:
            Category: The updated category or None if the category does not exist.

        Raises:
            SQLAlchemyError: If a database operation fails.
        """
        try:
            category = self.db.query(Category).filter(Category.id == category_id).first()
            if category:
                category.name = category_data.name
                self.db.commit()
                self.db.refresh(category)
                return category
            return None
        except SQLAlchemyError as e:
            raise SQLAlchemyError(f"Failed to update category due to: {e}")

    def delete(self, category_id: int) -> bool:
        """
        Deletes a category by its ID.

        Args:
            category_id (int): The ID of the category to delete.

        Returns:
            bool: True if the category was successfully deleted, False otherwise.

        Raises:
            SQLAlchemyError: If a database operation fails.
        """
        try:
            category = self.db.query(Category).filter(Category.id == category_id).first()
            if category:
                self.db.delete(category)
                self.db.commit()
                return True
            return False
        except SQLAlchemyError as e:
            raise SQLAlchemyError(f"Failed to delete category due to: {e}")
        
    def get_category_id_and_names(self) -> list:
        """
        Retrieves the IDs and names of all categories.

        Returns:
            list of tuples: A list of tuples, where each tuple contains (id, name) of a category.

        Raises:
            SQLAlchemyError: If a database operation fails.
        """
        try:
            categories = self.db.query(Category.id, Category.name).all()
            return categories
        except SQLAlchemyError as e:
            raise SQLAlchemyError(f"Failed to retrieve category IDs and names due to: {e}")

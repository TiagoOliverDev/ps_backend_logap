from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from app.schemas.category_schema import CategoryCreate, Category
from app.repositories.category_repository import CategoryRepository

class CategoryService:
    def __init__(self, db: Session):
        """
        Initializes the CategoryService with a database session and attaches a CategoryRepository.

        Args:
            db (Session): The SQLAlchemy session for database interaction.
        """
        self.repository = CategoryRepository(db)

    def create_category(self, category_data: CategoryCreate) -> Category:
        """
        Creates a new category using the provided category data.

        Args:
            category_data (CategoryCreate): Data used to create a new category.

        Returns:
            Category: The newly created category instance.

        Raises:
            SQLAlchemyError: If a database error occurs during the creation process.
        """
        try:
            return self.repository.create(category_data)
        except SQLAlchemyError as e:
            raise Exception(f"Failed to create category due to database error: {e}")

    def get_category(self, category_id: int) -> Category:
        """
        Retrieves a category by its ID.

        Args:
            category_id (int): The ID of the category to retrieve.

        Returns:
            Category: The retrieved category, or None if not found.

        Raises:
            SQLAlchemyError: If a database error occurs during the retrieval process.
        """
        try:
            return self.repository.get_by_id(category_id)
        except SQLAlchemyError as e:
            raise Exception(f"Failed to retrieve category due to database error: {e}")

    def get_categories(self) -> list:
        """
        Retrieves all categories from the database.

        Returns:
            list of Category: A list of categories.

        Raises:
            SQLAlchemyError: If a database error occurs during the retrieval process.
        """
        try:
            return self.repository.get_all()
        except SQLAlchemyError as e:
            raise Exception(f"Failed to retrieve all categories due to database error: {e}")

    def update_category(self, category_id: int, category_data: CategoryCreate) -> Category:
        """
        Updates an existing category with new data.

        Args:
            category_id (int): The ID of the category to update.
            category_data (CategoryCreate): New data for the category.

        Returns:
            Category: The updated category, or None if the category does not exist.

        Raises:
            SQLAlchemyError: If a database error occurs during the update process.
        """
        try:
            return self.repository.update(category_id, category_data)
        except SQLAlchemyError as e:
            raise Exception(f"Failed to update category due to database error: {e}")

    def delete_category(self, category_id: int) -> bool:
        """
        Deletes a category by its ID.

        Args:
            category_id (int): The ID of the category to delete.

        Returns:
            bool: True if the category was successfully deleted, False otherwise.

        Raises:
            SQLAlchemyError: If a database error occurs during the deletion process.
        """
        try:
            return self.repository.delete(category_id)
        except SQLAlchemyError as e:
            raise Exception(f"Failed to delete category due to database error: {e}")

from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from app.schemas.product_schema import ProductCreate, Product
from app.repositories.product_repository import ProductRepository

class ProductService:
    def __init__(self, db: Session):
        """
        Initializes the ProductService with a database session and attaches a ProductRepository for database operations.

        Args:
            db (Session): The SQLAlchemy session for database interaction.
        """
        self.repository = ProductRepository(db)

    def create_product(self, product_data: ProductCreate) -> Product:
        """
        Creates a new product using the provided product data.

        Args:
            product_data (ProductCreate): Data used to create a new product.

        Returns:
            Product: The newly created product instance.

        Raises:
            SQLAlchemyError: If a database error occurs.
        """
        try:
            return self.repository.create(product_data)
        except SQLAlchemyError as e:
            raise Exception(f"Failed to create product due to database error: {e}")

    def get_product(self, product_id: int) -> Product:
        """
        Retrieves a product by its ID.

        Args:
            product_id (int): The ID of the product to retrieve.

        Returns:
            Product: The retrieved product, or None if not found.

        Raises:
            SQLAlchemyError: If a database error occurs.
        """
        try:
            return self.repository.get_by_id(product_id)
        except SQLAlchemyError as e:
            raise Exception(f"Failed to retrieve product due to database error: {e}")

    def get_products(self) -> list:
        """
        Retrieves all products from the database.

        Returns:
            list of Product: A list of products.

        Raises:
            SQLAlchemyError: If a database error occurs.
        """
        try:
            return self.repository.get_all()
        except SQLAlchemyError as e:
            raise Exception(f"Failed to retrieve all products due to database error: {e}")

    def update_product(self, product_id: int, product_data: ProductCreate) -> Product:
        """
        Updates an existing product with new data.

        Args:
            product_id (int): The ID of the product to update.
            product_data (ProductCreate): The new data for the product.

        Returns:
            Product: The updated product, or None if the product does not exist.

        Raises:
            SQLAlchemyError: If a database error occurs.
        """
        try:
            return self.repository.update(product_id, product_data)
        except SQLAlchemyError as e:
            raise Exception(f"Failed to update product due to database error: {e}")

    def delete_product(self, product_id: int) -> bool:
        """
        Deletes a product by its ID.

        Args:
            product_id (int): The ID of the product to delete.

        Returns:
            bool: True if the product was successfully deleted, False otherwise.

        Raises:
            SQLAlchemyError: If a database error occurs.
        """
        try:
            return self.repository.delete(product_id)
        except SQLAlchemyError as e:
            raise Exception(f"Failed to delete product due to database error: {e}")

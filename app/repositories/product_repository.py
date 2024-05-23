from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from app.models.models import Product
from app.schemas.product_schema import ProductCreate

class ProductRepository:
    def __init__(self, db: Session):
        """
        Initializes the ProductRepository with a database session.

        Args:
            db (Session): The SQLAlchemy session for database interaction.
        """
        self.db = db

    def create(self, product_data: ProductCreate) -> Product:
        """
        Create a new product using the provided product data.

        Args:
            product_data (ProductCreate): Data used to create a new product.

        Returns:
            Product: The newly created product instance.

        Raises:
            SQLAlchemyError: If any database operation fails.
        """
        try:
            product = Product(**product_data.dict())
            self.db.add(product)
            self.db.commit()
            self.db.refresh(product)
            return product
        except SQLAlchemyError as e:
            raise SQLAlchemyError(f"Failed to create product due to: {e}")

    def get_by_id(self, product_id: int) -> Product:
        """
        Retrieve a product by its ID.

        Args:
            product_id (int): The ID of the product to retrieve.

        Returns:
            Product: The retrieved product or None if not found.
        """
        try:
            return self.db.query(Product).filter(Product.id == product_id).first()
        except SQLAlchemyError as e:
            raise SQLAlchemyError(f"Failed to retrieve product due to: {e}")

    def get_all(self) -> list:
        """
        Retrieve all products.

        Returns:
            list: A list of all products.
        """
        try:
            return self.db.query(Product).all()
        except SQLAlchemyError as e:
            raise SQLAlchemyError(f"Failed to retrieve all products due to: {e}")

    def update(self, product_id: int, product_data: ProductCreate) -> Product:
        """
        Update an existing product with the provided data.

        Args:
            product_id (int): The ID of the product to update.
            product_data (ProductCreate): New data for the product.

        Returns:
            Product: The updated product or None if the product does not exist.

        Raises:
            SQLAlchemyError: If any database operation fails.
        """
        try:
            product = self.db.query(Product).filter(Product.id == product_id).first()
            if product:
                for var, value in product_data.dict().items():
                    setattr(product, var, value)
                self.db.commit()
                self.db.refresh(product)
                return product
            return None
        except SQLAlchemyError as e:
            raise SQLAlchemyError(f"Failed to update product due to: {e}")

    def delete(self, product_id: int) -> bool:
        """
        Delete a product by its ID.

        Args:
            product_id (int): The ID of the product to delete.

        Returns:
            bool: True if the product was successfully deleted, False otherwise.

        Raises:
            SQLAlchemyError: If any database operation fails.
        """
        try:
            product = self.db.query(Product).filter(Product.id == product_id).first()
            if product:
                self.db.delete(product)
                self.db.commit()
                return True
            return False
        except SQLAlchemyError as e:
            raise SQLAlchemyError(f"Failed to delete product due to: {e}")

from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from app.repositories.supplier_repository import SupplierRepository
from app.schemas.supplier_schema import SupplierCreate, Supplier
from app.exceptions import DatabaseOperationError, NotFoundError

class SupplierService:
    def __init__(self, db: Session):
        """
        Initializes the supplier service with a database session.
        
        Args:
            db (Session): The SQLAlchemy database session.
        """
        self.repository = SupplierRepository(db)

    def create_supplier(self, supplier_data: SupplierCreate) -> Supplier:
        """
        Creates a new supplier using the provided data.

        Args:
            supplier_data (SupplierCreate): The data required to create a supplier.

        Returns:
            Supplier: The newly created supplier instance.

        Raises:
            DatabaseOperationError: If a database error occurs during creation.
        """
        try:
            return self.repository.create(supplier_data)
        except SQLAlchemyError as e:
            raise DatabaseOperationError(e)

    def update_supplier(self, supplier_id: int, supplier_data: SupplierCreate) -> Supplier:
        """
        Updates an existing supplier identified by the given supplier ID with the provided data.

        Args:
            supplier_id (int): The ID of the supplier to update.
            supplier_data (SupplierCreate): The data to update the supplier with.

        Returns:
            Supplier: The updated supplier instance, or None if not found.

        Raises:
            DatabaseOperationError: If a database error occurs during the update.
            NotFoundError: If no supplier is found with the provided ID.
        """
        try:
            updated_supplier = self.repository.update(supplier_id, supplier_data)
            if updated_supplier is None:
                raise NotFoundError("Supplier", supplier_id)
            return updated_supplier
        except SQLAlchemyError as e:
            raise DatabaseOperationError(e)

    def get_supplier(self, supplier_id: int) -> Supplier:
        """
        Retrieves a supplier by its ID.

        Args:
            supplier_id (int): The ID of the supplier to retrieve.

        Returns:
            Supplier: The retrieved supplier instance, or None if not found.

        Raises:
            NotFoundError: If no supplier is found with the specified ID.
        """
        supplier = self.repository.get_by_id(supplier_id)
        if not supplier:
            raise NotFoundError("Supplier", supplier_id)
        return supplier

    def get_suppliers(self) -> list:
        """
        Retrieves a list of suppliers with an optional limit on the number of results.

        Returns:
            list of Supplier: A list of suppliers.
        """
        return self.repository.get_all()

    def delete_supplier(self, supplier_id: int) -> bool:
        """
        Deletes a supplier identified by its ID.

        Args:
            supplier_id (int): The ID of the supplier to delete.

        Returns:
            bool: True if the supplier was successfully deleted, False otherwise.

        Raises:
            NotFoundError: If no supplier is found with the specified ID.
            DatabaseOperationError: If a database error occurs during deletion.
        """
        try:
            if not self.repository.delete(supplier_id):
                raise NotFoundError("Supplier", supplier_id)
            return True
        except SQLAlchemyError as e:
            raise DatabaseOperationError(e)

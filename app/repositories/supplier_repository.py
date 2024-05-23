# app/repositories/supplier_repository.py
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from app.models.models import Supplier
from app.schemas.supplier_schema import SupplierCreate

class SupplierRepository:
    def __init__(self, db: Session):
        """Initialize the repository with the database session."""
        self.db = db

    def create(self, supplier_data: SupplierCreate) -> Supplier:
        """Creates a new supplier entry in the database.
        
        Args:
            supplier_data (SupplierCreate): The schema containing all required fields to create a supplier.
        
        Returns:
            Supplier: The newly created supplier object.
        
        Raises:
            SQLAlchemyError: An error occurred while performing database operations.
        """
        try:
            supplier = Supplier(**supplier_data.dict())
            self.db.add(supplier)
            self.db.commit()
            self.db.refresh(supplier)
            return supplier
        except SQLAlchemyError as e:
            self.db.rollback()
            raise ValueError(f"Error creating supplier: {e}")

    def update(self, supplier_id: int, supplier_data: SupplierCreate) -> Supplier:
        """Updates an existing supplier.
        
        Args:
            supplier_id (int): The ID of the supplier to update.
            supplier_data (SupplierCreate): The schema with updated fields for the supplier.
        
        Returns:
            Supplier or None: The updated supplier object, or None if no supplier was found.
        
        Raises:
            SQLAlchemyError: An error occurred while performing database operations.
        """
        try:
            supplier = self.db.query(Supplier).filter(Supplier.id == supplier_id).first()
            if supplier:
                supplier.name = supplier_data.name
                supplier.email = supplier_data.email
                supplier.phone = supplier_data.phone
                self.db.commit()
                self.db.refresh(supplier)
                return supplier
            return None
        except SQLAlchemyError as e:
            self.db.rollback()
            raise ValueError(f"Error updating supplier with ID {supplier_id}: {e}")

    def get_all(self, skip: int = 0, limit: int = 10) -> list:
        """Retrieves all suppliers from the database with pagination.
        
        Args:
            skip (int): Number of entries to skip (for pagination).
            limit (int): Maximum number of entries to return.
        
        Returns:
            list: A list of suppliers.
        """
        return self.db.query(Supplier).offset(skip).limit(limit).all()
    
    def get_by_id(self, supplier_id: int) -> Supplier:
        """Fetches a single supplier by its ID.
        
        Args:
            supplier_id (int): The ID of the supplier to retrieve.
        
        Returns:
            Supplier or None: The supplier object if found, otherwise None.
        """
        return self.db.query(Supplier).filter(Supplier.id == supplier_id).first()

    def delete(self, supplier_id: int) -> bool:
        """Deletes a supplier from the database.
        
        Args:
            supplier_id (int): The ID of the supplier to delete.
        
        Returns:
            bool: True if the supplier was deleted, False otherwise.
        
        Raises:
            SQLAlchemyError: An error occurred while performing database operations.
        """
        try:
            supplier = self.db.query(Supplier).filter(Supplier.id == supplier_id).first()
            if supplier:
                self.db.delete(supplier)
                self.db.commit()
                return True
            return False
        except SQLAlchemyError as e:
            self.db.rollback()
            raise ValueError(f"Error deleting supplier with ID {supplier_id}: {e}")

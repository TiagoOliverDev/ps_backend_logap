# app/services/supplier_service.py
from sqlalchemy.orm import Session
from app.schemas.supplier_schema import SupplierCreate, Supplier
from app.repositories.supplier_repository import SupplierRepository

class SupplierService:
    def __init__(self, db: Session):
        self.repository = SupplierRepository(db)

    def create_supplier(self, supplier_data: SupplierCreate) -> Supplier:
        return self.repository.create(supplier_data)

    def update_supplier(self, supplier_id: int, supplier_data: SupplierCreate) -> Supplier:
        return self.repository.update(supplier_id, supplier_data)

    def get_supplier(self, supplier_id: int) -> Supplier:
        return self.repository.get_by_id(supplier_id)
                    
    def get_suppliers(self, skip: int = 0, limit: int = 10) -> list:
        return self.repository.get_all(skip, limit)

    def delete_supplier(self, supplier_id: int) -> bool:
        return self.repository.delete(supplier_id)

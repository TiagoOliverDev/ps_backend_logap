# app/repositories/supplier_repository.py
from sqlalchemy.orm import Session
from app.models.models import Supplier
from app.schemas.supplier_schema import SupplierCreate

class SupplierRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, supplier_data: SupplierCreate):
        supplier = Supplier(**supplier_data.dict())
        self.db.add(supplier)
        self.db.commit()
        self.db.refresh(supplier)
        return supplier

    def update(self, supplier_id: int, supplier_data: SupplierCreate):
        supplier = self.db.query(Supplier).filter(Supplier.id == supplier_id).first()
        if supplier:
            supplier.name = supplier_data.name
            supplier.email = supplier_data.email
            supplier.phone = supplier_data.phone
            self.db.commit()
            self.db.refresh(supplier)
            return supplier
        return None

    def get_all(self, skip: int = 0, limit: int = 10):
        return self.db.query(Supplier).offset(skip).limit(limit).all()
    
    def get_by_id(self, supplier_id: int):
        return self.db.query(Supplier).filter(Supplier.id == supplier_id).first()

    def delete(self, supplier_id: int):
        supplier = self.db.query(Supplier).filter(Supplier.id == supplier_id).first()
        if supplier:
            self.db.delete(supplier)
            self.db.commit()
            return True
        return False

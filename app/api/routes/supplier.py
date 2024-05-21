# app/api/routes/supplier.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.schemas.supplier_schema import Supplier, SupplierCreate
from app.services.supplier_service import SupplierService
from app.api.dependencies import get_db

router = APIRouter()

@router.post("/", response_model=Supplier)
def create_supplier(supplier_data: SupplierCreate, db: Session = Depends(get_db)):
    supplier_service = SupplierService(db)
    return supplier_service.create_supplier(supplier_data)

@router.get("/{supplier_id}", response_model=Supplier)
def read_supplier(supplier_id: int, db: Session = Depends(get_db)):
    supplier_service = SupplierService(db)
    supplier = supplier_service.get_supplier(supplier_id)
    if supplier is None:
        raise HTTPException(status_code=404, detail="Fornecedor não encontrado")
    return supplier

@router.get("/", response_model=List[Supplier])
def read_suppliers(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    supplier_service = SupplierService(db)
    return supplier_service.get_suppliers(skip, limit)

@router.put("/{supplier_id}", response_model=Supplier)
def update_supplier(supplier_id: int, supplier_data: SupplierCreate, db: Session = Depends(get_db)):
    supplier_service = SupplierService(db)
    updated_supplier = supplier_service.update_supplier(supplier_id, supplier_data)
    if updated_supplier is None:
        raise HTTPException(status_code=404, detail="Fornecedor não encontrado")
    return updated_supplier

@router.delete("/{supplier_id}", status_code=204)
def delete_supplier(supplier_id: int, db: Session = Depends(get_db)):
    supplier_service = SupplierService(db)
    if not supplier_service.delete_supplier(supplier_id):
        raise HTTPException(status_code=404, detail="Fornecedor não encontrado")
    return {"detail": "Fornecedor deletado com sucesso"}

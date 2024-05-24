from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from typing import List
from app.schemas.supplier_schema import Supplier, SupplierCreate
from app.services.supplier_service import SupplierService
from app.api.dependencies import get_db

router = APIRouter()

@router.post("/cadastrar", response_model=Supplier, status_code=201)
def create_supplier(supplier_data: SupplierCreate, db: Session = Depends(get_db)):
    """
    Create a new supplier with the provided data.
    
    Args:
        supplier_data (SupplierCreate): The supplier data to create a new supplier.
        db (Session, optional): Dependency injection of the database session.
    
    Returns:
        Supplier: The created supplier object.
    
    Raises:
        HTTPException: 400 error if supplier creation fails for any reason related to data validation or database operations.
    """
    supplier_service = SupplierService(db)
    try:
        return supplier_service.create_supplier(supplier_data)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/{supplier_id}", response_model=Supplier)
def read_supplier(supplier_id: int, db: Session = Depends(get_db)):
    """
    Retrieve a supplier by their ID. Returns the supplier details if found.
    
    Args:
        supplier_id (int): The unique identifier for the supplier.
        db (Session, optional): Dependency injection of the database session.
    
    Returns:
        Supplier: The retrieved supplier object.
    
    Raises:
        HTTPException: 404 error if no supplier is found with the provided ID.
        HTTPException: 500 error if there is a database related error.
    """
    try:
        supplier_service = SupplierService(db)
        supplier = supplier_service.get_supplier(supplier_id)
        if supplier is None:
            raise HTTPException(status_code=404, detail="Supplier not found")
        return supplier
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail="An unexpected error occurred")

@router.get("/fornecedores/listagem", response_model=List[Supplier])
def read_suppliers(db: Session = Depends(get_db)):
    """
    Retrieve a list of suppliers. 
    
    Args:
        db (Session, optional): Dependency injection of the database session.
    
    Returns:
        List[Supplier]: A list of suppliers.
    
    Raises:
        HTTPException: 500 error if there is a database related error or any other unexpected error.
    """
    try:
        supplier_service = SupplierService(db)
        return supplier_service.get_suppliers()
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail="An unexpected error occurred")

@router.put("/editar/{supplier_id}", response_model=Supplier)
def update_supplier(supplier_id: int, supplier_data: SupplierCreate, db: Session = Depends(get_db)):
    """
    Update a supplier identified by their ID with the provided data. Returns the updated supplier object if successful.
    
    Args:
        supplier_id (int): The unique identifier for the supplier.
        supplier_data (SupplierCreate): The new data for updating the supplier.
        db (Session, optional): Dependency injection of the database session.
    
    Returns:
        Supplier: The updated supplier object.
    
    Raises:
        HTTPException: 404 error if no supplier is found with the provided ID.
        HTTPException: 500 error if there is a database related error or any other unexpected error.
    """
    try:
        supplier_service = SupplierService(db)
        updated_supplier = supplier_service.update_supplier(supplier_id, supplier_data)
        if updated_supplier is None:
            raise HTTPException(status_code=404, detail="Supplier not found")
        return updated_supplier
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail="An unexpected error occurred")

@router.delete("/delete/{supplier_id}", status_code=204)
def delete_supplier(supplier_id: int, db: Session = Depends(get_db)):
    """
    Delete a supplier identified by their ID. Returns a confirmation message if successful.
    
    Args:
        supplier_id (int): The unique identifier for the supplier.
        db (Session, optional): Dependency injection of the database session.
    
    Returns:
        dict: A confirmation message of deletion.
    
    Raises:
        HTTPException: 404 error if no supplier is found with the provided ID.
        HTTPException: 500 error if there is a database related error or any other unexpected error.
    """
    try:
        supplier_service = SupplierService(db)
        if not supplier_service.delete_supplier(supplier_id):
            raise HTTPException(status_code=404, detail="Supplier not found")
        return {"detail": "Supplier successfully deleted"}
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail="An unexpected error occurred")
# app/api/routes/category.py
from fastapi import APIRouter, Depends, HTTPException, Response
from typing import List
from sqlalchemy.orm import Session
from app.schemas.category_schema import Category, CategoryCreate
from app.services.category_service import CategoryService
from app.api.dependencies import get_db

router = APIRouter()

@router.post("/criar", response_model=Category)
def create_category(category_data: CategoryCreate, db: Session = Depends(get_db)):
    category_service = CategoryService(db)
    return category_service.create_category(category_data)

@router.get("/{category_id}", response_model=Category)
def read_category(category_id: int, db: Session = Depends(get_db)):
    category_service = CategoryService(db)
    category = category_service.get_category(category_id)
    if category is None:
        raise HTTPException(status_code=404, detail="Categoria não encontrada")
    return category

@router.get("/listagem", response_model=List[Category])
def read_categories(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    category_service = CategoryService(db)
    return category_service.get_categories(skip, limit)

@router.put("/editar/{category_id}", response_model=Category)
def update_category(category_id: int, category_data: CategoryCreate, db: Session = Depends(get_db)):
    category_service = CategoryService(db)
    updated_category = category_service.update_category(category_id, category_data)
    if updated_category is None:
        raise HTTPException(status_code=404, detail="Categoria não encontrada")
    return updated_category

@router.delete("/delete/{category_id}", status_code=204)
def delete_category(category_id: int, db: Session = Depends(get_db)):
    category_service = CategoryService(db)
    if not category_service.delete_category(category_id):
        raise HTTPException(status_code=404, detail="Categoria não encontrada")
    return Response(status_code=204)

from fastapi import APIRouter, Depends, HTTPException, Response
from typing import List, Tuple
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from app.schemas.category_schema import Category, CategoryCreate
from app.services.category_service import CategoryService
from app.api.dependencies import get_db

router = APIRouter()

@router.post("/cadastrar", response_model=Category, status_code=201)
def create_category(category_data: CategoryCreate, db: Session = Depends(get_db)) -> Category:
    """
    Create a new category with the provided category data.
    
    Args:
        category_data (CategoryCreate): The data used to create a new category.
        db (Session): Dependency injection of the database session.
    
    Returns:
        Category: The newly created category object.
    
    Raises:
        HTTPException: 500 error if there is a problem creating the category.
    """
    category_service = CategoryService(db)
    try:
        return category_service.create_category(category_data)
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=f"Failed to create category: {e}")

@router.get("/{category_id}", response_model=Category)
def read_category(category_id: int, db: Session = Depends(get_db)) -> Category:
    """
    Retrieve a specific category by its ID.
    
    Args:
        category_id (int): The unique identifier for the category.
        db (Session): Dependency injection of the database session.
    
    Returns:
        Category: The retrieved category object or None if not found.
    
    Raises:
        HTTPException: 404 error if no category is found.
    """
    category_service = CategoryService(db)
    category = category_service.get_category(category_id)
    if category is None:
        raise HTTPException(status_code=404, detail="Categoria não encontrada")
    return category

@router.get("/categorias/listagem", response_model=List[Category])
def read_categories(db: Session = Depends(get_db)) -> List[Category]:
    """
    Retrieve a list of categories.
    
    Args:
        db (Session): Dependency injection of the database session.
    
    Returns:
        List[Category]: A list of categories.
    
    Raises:
        HTTPException: 500 error if there is a problem retrieving the categories.
    """
    category_service = CategoryService(db)
    try:
        return category_service.get_categories()
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=f"Failed to retrieve categories: {e}")

@router.put("/editar/{category_id}", response_model=Category)
def update_category(category_id: int, category_data: CategoryCreate, db: Session = Depends(get_db)) -> Category:
    """
    Update an existing category with new data.
    
    Args:
        category_id (int): The unique identifier for the category.
        category_data (CategoryCreate): New data for updating the category.
        db (Session): Dependency injection of the database session.
    
    Returns:
        Category: The updated category object or None if not found.
    
    Raises:
        HTTPException: 404 error if the category is not found.
        HTTPException: 500 error if there is a problem updating the category.
    """
    category_service = CategoryService(db)
    updated_category = category_service.update_category(category_id, category_data)
    if updated_category is None:
        raise HTTPException(status_code=404, detail="Categoria não encontrada")
    return updated_category

@router.delete("/delete/{category_id}", status_code=204)
def delete_category(category_id: int, db: Session = Depends(get_db)) -> Response:
    """
    Delete a category by its ID.
    
    Args:
        category_id (int): The unique identifier for the category.
        db (Session): Dependency injection of the database session.
    
    Returns:
        Response: A 204 No Content response indicating successful deletion.
    
    Raises:
        HTTPException: 404 error if the category is not found.
    """
    category_service = CategoryService(db)
    if not category_service.delete_category(category_id):
        raise HTTPException(status_code=404, detail="Categoria não encontrada")
    return Response(status_code=204)

@router.get("/categorias/nomes", response_model=List[Tuple[int, str]])
def get_category_id_and_names(db: Session = Depends(get_db)) -> List:
    """
    Retrieve a list of category IDs and names.

    Returns:
        List[Tuple[int, str]]: A list of tuples, each containing the ID and name of a category.

    Raises:
        HTTPException: 500 error if there is a problem retrieving the category names.
    """
    category_service = CategoryService(db)
    try:
        category_id_and_names = category_service.get_category_id_and_names()
        return category_id_and_names
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to retrieve category names: {e}")

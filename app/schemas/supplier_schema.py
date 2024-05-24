from pydantic import BaseModel, EmailStr

class SupplierBase(BaseModel):
    name: str
    email: EmailStr
    phone: str

class SupplierCreate(SupplierBase):
    pass

class Supplier(SupplierBase):
    id: int

    class Config:
        from_attributes = True

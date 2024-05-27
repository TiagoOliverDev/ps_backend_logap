from sqlalchemy import Column, Integer, String, ForeignKey, DECIMAL
from sqlalchemy.orm import relationship
from app.db.database import Base
from werkzeug.security import check_password_hash


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)

    def __repr__(self):
        return f"<User(id={self.id}, email={self.email})>"
    
    def check_password(self, password: str) -> bool:
        """Verify the provided password against the stored hash."""
        return check_password_hash(self.password, password)
    
class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    products = relationship("Product", back_populates="category")

class Supplier(Base):
    __tablename__ = "suppliers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    phone = Column(String, unique=True, index=True)
    products = relationship("Product", back_populates="supplier")

class Product(Base):
    __tablename__ = "products"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    purchase_price = Column(DECIMAL(10, 2))
    quantity = Column(Integer)
    sale_price = Column(DECIMAL(10, 2))
    category_id = Column(Integer, ForeignKey("categories.id"))
    supplier_id = Column(Integer, ForeignKey("suppliers.id"))

    category = relationship("Category", back_populates="products")
    supplier = relationship("Supplier", back_populates="products")

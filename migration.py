import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from sqlalchemy import create_engine
from app.db.database import Base, SQLALCHEMY_DATABASE_URL
from app.models.models import Category, Supplier, Product  

def init_db():
    """Cria o banco de dados e todas as tabelas definidas nos modelos."""
    engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
    Base.metadata.create_all(engine)
    print("Database and tables created!")

if __name__ == "__main__":
    init_db()

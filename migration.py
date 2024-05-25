import os
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.db.database import Base

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app.models.models import Category, Supplier, Product

# URLs dos bancos de produção e testes
SQLALCHEMY_DATABASE_URL = "sqlite:///{}".format(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'app/db/prod.db'))
SQLALCHEMY_TEST_DATABASE_URL = "sqlite:///{}".format(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'app/db/test.db'))

def init_db(db_url):
    """Cria o banco de dados e todas as tabelas definidas nos modelos."""
    engine = create_engine(db_url, connect_args={"check_same_thread": False})
    Base.metadata.create_all(engine)
    print(f"Database and tables created at {db_url}!")

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == 'test':
        init_db(SQLALCHEMY_TEST_DATABASE_URL)
    else:
        init_db(SQLALCHEMY_DATABASE_URL)

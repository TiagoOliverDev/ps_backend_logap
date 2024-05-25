from app.db.database import SessionLocal
from app.db.test_database import TestSessionLocal

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_db_test():
    db = TestSessionLocal()
    try:
        yield db
    finally:
        db.close()
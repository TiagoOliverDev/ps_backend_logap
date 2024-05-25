import unittest
from fastapi.testclient import TestClient
from app.main import app
from app.models.models import Category
from app.api.dependencies import get_db
from app.db.test_database import create_test_database, TestSessionLocal, Base

client = TestClient(app)

class TestCategoryEndpoints(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        create_test_database()

    def setUp(self):
        self.db = TestSessionLocal()
        Base.metadata.create_all(bind=self.db.get_bind())
        self.client = TestClient(app)
        app.dependency_overrides[get_db] = lambda: self.db

    def tearDown(self):
        self.db.close()
        app.dependency_overrides[get_db] = get_db

    def test_create_category(self):
        response = self.client.post("/categories/cadastrar", json={"name": "teste"})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json()['name'], 'teste')

        category_id = response.json()['id']
        self.db.query(Category).filter(Category.id == category_id).delete()
        self.db.commit()

    def test_read_category(self):
        sample_category = Category(name="teste")
        self.db.add(sample_category)
        self.db.commit()
        self.db.refresh(sample_category)

        response = self.client.get(f"/categories/{sample_category.id}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['name'], "teste")

        self.db.query(Category).filter(Category.id == sample_category.id).delete()
        self.db.commit()

    def test_read_categories(self):
        sample_category = Category(name="teste")
        self.db.add(sample_category)
        self.db.commit()
        self.db.refresh(sample_category)

        response = self.client.get("/categories/categorias/listagem")
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)
        self.assertEqual(len(response.json()), 1)

        self.db.query(Category).filter(Category.id == sample_category.id).delete()
        self.db.commit()

    def test_update_category(self):
        sample_category = Category(name="teste")
        self.db.add(sample_category)
        self.db.commit()
        self.db.refresh(sample_category)

        response = self.client.put(f"/categories/editar/{sample_category.id}", json={"name": "Teste editado"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['name'], "Teste editado")

        self.db.query(Category).filter(Category.id == sample_category.id).delete()
        self.db.commit()

    def test_delete_category(self):
        sample_category = Category(name="teste")
        self.db.add(sample_category)
        self.db.commit()
        self.db.refresh(sample_category)

        response = self.client.delete(f"/categories/delete/{sample_category.id}")
        self.assertEqual(response.status_code, 204)

if __name__ == "__main__":
    unittest.main()

import unittest
from unittest.mock import patch, MagicMock
from fastapi import HTTPException
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from app.main import app

client = TestClient(app)

class TestCategoryEndpoints(unittest.TestCase):
    @patch('app.api.dependencies.get_db')
    def test_create_category(self, mocked_get_db):
        db = MagicMock()
        mocked_get_db.return_value = db
        db.commit = MagicMock()

        response = client.post("/categories/cadastrar", json={"name": "Eletrônicos", "description": "Categoria de produtos eletrônicos"})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json()['name'], 'Eletrônicos')

    @patch('app.api.dependencies.get_db')
    def test_read_category(self, mocked_get_db):
        db = MagicMock()
        mocked_get_db.return_value = db

        response = client.get("/1")
        self.assertEqual(response.status_code, 200)

    @patch('app.api.dependencies.get_db')
    def test_read_categories(self, mocked_get_db):
        db = MagicMock()
        mocked_get_db.return_value = db

        response = client.get("/categorias/listagem")
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)

    @patch('app.api.dependencies.get_db')
    def test_update_category(self, mocked_get_db):
        db = MagicMock()
        mocked_get_db.return_value = db
        db.commit = MagicMock()

        response = client.put("/editar/1", json={"name": "Livros", "description": "Categoria de livros"})
        self.assertEqual(response.status_code, 200)

    @patch('app.api.dependencies.get_db')
    def test_delete_category(self, mocked_get_db):
        db = MagicMock()
        mocked_get_db.return_value = db
        db.commit = MagicMock()

        response = client.delete("/delete/1")
        self.assertEqual(response.status_code, 204)

if __name__ == '__main__':
    unittest.main()

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

        response = client.post("/categories/cadastrar", json={"name": "todes", "description": "Categoria de livros"})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json()['name'], 'Livros')

    @patch('app.api.dependencies.get_db')
    def test_read_category(self, mocked_get_db):
        db = MagicMock()
        mocked_get_db.return_value = db

        response = client.get("/categories/3")
        self.assertEqual(response.status_code, 200)

    @patch('app.api.dependencies.get_db')
    def test_read_categories(self, mocked_get_db):
        db = MagicMock()
        mocked_get_db.return_value = db

        response = client.get("/categories/categorias/listagem")
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)

    @patch('app.api.dependencies.get_db')
    def test_update_category(self, mocked_get_db):
        db = MagicMock()
        mocked_get_db.return_value = db
        db.commit = MagicMock()

        response = client.put("/categories/editar/7", json={"name": "Teste", "description": "teste"})
        self.assertEqual(response.status_code, 200)

    @patch('app.api.dependencies.get_db')
    def test_delete_category(self, mocked_get_db):
        db = MagicMock()
        mocked_get_db.return_value = db
        db.commit = MagicMock()

        response = client.delete("/categories/delete/7")
        self.assertEqual(response.status_code, 204)

if __name__ == '__main__':
    unittest.main()

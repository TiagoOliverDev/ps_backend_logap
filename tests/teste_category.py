import requests

# Configuração inicial
BASE_URL = "http://localhost:8080/categories"

def test_create_category():
    """Testa a criação de uma nova categoria."""

    new_category = {"name": "Liquidos"}
    response = requests.post(f"{BASE_URL}/criar", json=new_category)
    print("Create Response:", response.text)
    category_id = response.json()['id']
    print('res:', category_id)

def test_get_category(category_id):
    """Testa a obtenção de uma categoria pelo ID."""
    response = requests.get(f"{BASE_URL}/{category_id}")
    print("Read Status Code:", response.status_code)
    print("Read Response:", response.text)

def test_update_category(category_id):
    """Testa a atualização de uma categoria."""
    update_data = {"name": "Cereal Atualizado"}
    response = requests.put(f"{BASE_URL}/editar/{category_id}", json=update_data)
    print("Update Status Code:", response.status_code)
    print("Update Response:", response.text)

def test_list_categories():
    """Testa a listagem de todas as categorias."""
    response = requests.get(f"{BASE_URL}/listagem")
    print("List Status Code:", response.status_code)
    print("List Response:", response.text)

def test_delete_category(category_id):
    """Testa a exclusão de uma categoria."""
    response = requests.delete(f"{BASE_URL}/delete/{category_id}")
    print("Delete Status Code:", response.status_code)
    print("Delete Response:", response.status_code)


if __name__ == "__main__":
    # category_id = test_create_category()  # Criação e retenção do ID para futuros testes
    # test_get_category(2)                  # Teste de leitura da categoria
    # test_update_category(2)     # Teste de atualização da categoria
    # test_list_categories()                # Teste de listagem de todas as categorias
    test_delete_category(2)     # Teste de exclusão da categoria
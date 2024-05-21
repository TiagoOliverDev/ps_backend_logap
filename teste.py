import requests

# Defina a URL base do seu endpoint
base_url = "http://localhost:8080/products"

# Dados do novo produto a ser criado
new_product = {
    "name": "PC gamer 2",
    "purchase_price": 102.99,
    "quantity": 10,
    "sale_price": 152.99,
    "category_id": 1,
    "supplier_id": 1
}

# Faça uma solicitação POST para criar o produto
response = requests.post(f"{base_url}/criar", json=new_product)

# Verifique a resposta
if response.status_code == 200:
    print("Produto criado com sucesso!", response.status_code)
    print("Dados do produto:", response.json())
else:
    print("Falha ao criar o produto. Status code:", response.status_code)
    print("Mensagem de erro:", response.text)

# Opcional: faça uma solicitação GET para listar os produtos
response = requests.get(f"{base_url}/listagem")
if response.status_code == 200:
    print("Listagem de produtos:")
    for product in response.json():
        print(product)
else:
    print("Falha ao listar os produtos. Status code:", response.status_code)
    print("Mensagem de erro:", response.text)

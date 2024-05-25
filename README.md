<h1 align="center">API Backend Teste Logap</h1>

Backend 

<hr/>

# Documentação SWAGGER integrada ( acessar em /docs )

![background](https://github.com/TiagoOliverDev/ps_backend_logap/blob/main/app/imgs/docApi.png)

<hr/>

# Design Patterns utilizado

Basicamente foi usado um tipo de MVC.

- Model representado pelo uso do SQLAlchemy
- Service funcionando como uma ponte entre os Controllers e o Repository
- Endpoints separados por módulos
- Repository que funciona como uma abstração do acesso aos dados, que facilita a comunicação com o banco de dados e realiza as querys
- Views retornando dados de requisições em formato JSON
- migrations com alembic


# Padrão de pastas

```
    ps_backend_logap/
    ├── alembic/
    ├── app/
    │   ├── __init__.py
    │   ├── api/
    │   └──── routes/
    │   ├── db/
    │   └── ...
    │   ├── imgs/
    │   └── ...
    │   ├── models/
    │   └── ...
    │   └── repositories/
    │   └── ...
    │   └── schemas/
    │   └── services/
    │   └── exceptions.py
    │   └── main.py
    ├── venv/
    │   └── ...
    ├── tests/
    │   └── ...
    ├── .env
    ├── .gitignore
    ├── alembic.ini
    ├── Dockerfile
    └── README.md
    ├── requirements.txt
    ├── server.py
 ```

# Features gerais


- Crud completo de categorias
- Crud completo de fornecedores
- Crud completo de produtos


<hr/>

# Tecnologias

Usei as seguintes tecnologias:

- Python >= 3.10.11
- FastApi
- Sqllite 
- SQLAlchemy
- swagger
- unitest
- uvicorn

<hr/>

# Passos para rodar o projeto

## Step 1: Clone o repositório

- Crie uma pasta na sua maquína local e copia o repositório

- Clone [repository](https://github.com/TiagoOliverDev/ps_backend_logap.git) na sua pasta

  ```
  git clone https://github.com/TiagoOliverDev/ps_backend_logap.git
  ```

- Navegue até o diretório `cd ps_backend_logap`

## Step 2: Criar uma env

# # windows

 python -m venv nome_da_env

 nome_da_env/Scripts/activate

 pip install -r requirements.txt


# # Linux

 python3 -m venv meu_venv

 source meu_venv/bin/activate

 pip install -r requirements.txt


## Step 3: Criar migrations 

  ```
  python migration.py
  ```


## Step 5: Rodar API

  Rode o comando para startar a API:

  ```
  python server.py
  ```

# Agora pode acessar o link abaixo e testar a API via interface Swagger (se quiser)

  ```
  http://127.0.0.1:8080/docs
  ```

<hr/>


## OBSERVAÇÃO: A questão 1 do teste pode ser resolvido via /docs no endpoint /teste

![background](https://github.com/TiagoOliverDev/ps_backend_logap/blob/main/app/imgs/image.png)


## Testes unitários básicos!


  Rode com:

  ```
  python -m unittest tests.teste_category

  ```

  ```
  python -m unittest tests.teste_category

  ```

## Autor

:man: **Tiago Oliveira**

- [GitHub](https://github.com/TiagoOliverDev/)
- [LinkedIn](https://www.linkedin.com/in/tiago-oliveira-49a2a6205/)

## 🤝 Contribua
- Contribuições, issues, e feature são bem vindas!
- Clique aqui para criar uma issue [issues page](https://github.com/TiagoOliverDev/ps_backend_logap/issues).

# Gostou do projeto ?
Der ⭐ se gostou!

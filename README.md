# back-end-store
Project example for Layered Architeture

# Structure

```
.
├── app/                              # Módulo principal da aplicação
│   ├── dependencies.py               # Dependências globais do FastAPI (DI, auth, etc.)
│   ├── __init__.py                   # Inicializa o pacote app
│   ├── main.py                       # Ponto de entrada da aplicação FastAPI
│   │
│   ├── models/                       # Modelos de domínio / ORM (se aplicável)
│   │
│   ├── repositories/                 # Camada de acesso a dados
│   │   ├── __init__.py               # Inicializa o pacote repositories
│   │   └── store_repository.py       # Repositório de Store (DB, memória, etc.)
│   │
│   ├── routes/                       # Definição das rotas HTTP
│   │   ├── __init__.py               # Inicializa o pacote routes
│   │   └── stores.py                 # Endpoints relacionados a Stores
│   │
│   ├── schemas/                      # Schemas Pydantic (DTOs de entrada/saída)
│   │   ├── __init__.py               # Inicializa o pacote schemas
│   │   └── store.py                  # Schemas de validação para Store
│   │
│   └── services/                     # Camada de serviços (regras de negócio)
│       ├── __init__.py               # Inicializa o pacote services
│       └── store_service.py          # Serviço com lógica de negócio de Store
│
├── README.md                         # Documentação do projeto
└── requirements.txt                  # Dependências do projeto

```
### How to run the project:

Create venv:

```
python -m venv venv

# or your python version in linux

python3 -m venv venv 

```

Activate venv:

```
# windows:

.\venv\Scripts\activate.bat.

# linux 

 source venv/bin/activate   

```

Install dependencies with pip:

```
pip install -r requirements.txt

```

Run the project with uvicorn (not unicorn! LOL)

```
uvicorn main:app --reload

```

This way you can access the Swagger documentation and test it

[Swagger](http://127.0.0.1:8000/docs)
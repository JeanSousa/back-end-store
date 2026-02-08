from fastapi import FastAPI

from app.routes import stores_router

app = FastAPI()

app.include_router(stores_router)


@app.get('/inicio')
def get_inicio():
    return { "Inicio": True }
from fastapi import FastAPI

app = FastAPI()


@app.get('/inicio')
def get_inicio():
    return { "Inicio": True }
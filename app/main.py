from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.api import api_router
from app.frontend.views import view_router

def get_application():
    app = FastAPI(
        title= "Gerenciador de Pedidos",
        version="v1.0.0",
        doc_url="/docs",
    )
    return app

app = get_application()

# Monta arquivos estáticos para servir como SSR
app.mount("/static", StaticFiles(directory="app/frontend/static"), name="static")

# Rotas da API
app.include_router(api_router, prefix="/api")
# Rotas do Frontend (views)
app.include_router(view_router)
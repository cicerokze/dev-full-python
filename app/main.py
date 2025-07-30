from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.api.main import api_router
from app.frontend.views import frontend_router

app = FastAPI()

# Mount static files for SSR
app.mount("/static", StaticFiles(directory="app/frontend/static"), name="static")

# Include routers
app.include_router(api_router, prefix="/api")
app.include_router(frontend_router)
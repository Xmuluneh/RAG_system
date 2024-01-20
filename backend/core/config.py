from fastapi import FastAPI
from views import main_router

def create_app():
    app = FastAPI()
    
    app.include_router(main_router)

    return app
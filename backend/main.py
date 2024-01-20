# main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.main import router as main_router

app = FastAPI()

# Enable CORS (Cross-Origin Resource Sharing)
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(main_router, prefix="/main", tags=["main"])

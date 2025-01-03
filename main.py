from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from controllers.ProductController import router as product_router
from controllers.PriceController import router as price_router
from controllers.StoreController import router as store_router


app = FastAPI()

# Configuration de CORS
origins = [
    "http://127.0.0.1:5500",  # Origine pour le front-end local
    "http://localhost:5500",  # Autre variation de localhost
    "http://127.0.0.1:3000",  # Si vous utilisez un autre port pour le front
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Autoriser uniquement ces origines
    allow_credentials=True,  # Autoriser les cookies ou credentials
    allow_methods=["*"],  # Autoriser toutes les méthodes HTTP (GET, POST, etc.)
    allow_headers=["*"],  # Autoriser tous les headers
)


app.include_router(price_router, prefix="/api/v1")
app.include_router(store_router, prefix="/api/v1")
app.include_router(product_router, prefix="/api/v1")


@app.get("/")
async def root():
    return {"message": "Welcome to the API!"}

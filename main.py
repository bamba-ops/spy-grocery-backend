from fastapi import FastAPI
from controllers.ProductController import router as product_router
from controllers.PriceController import router as price_router
from controllers.StoreController import router as store_router


app = FastAPI()

app.include_router(price_router, prefix="/api/v1")
app.include_router(store_router, prefix="/api/v1")
app.include_router(product_router, prefix="/api/v1")

@app.get("/")
async def root():
    return {"message": "Welcome to the API!"}
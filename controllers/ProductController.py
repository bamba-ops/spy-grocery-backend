from fastapi import APIRouter, HTTPException
from typing import List
from services.ProductService import ProductService
from models.product import Product

router = APIRouter()

@router.post("/product", response_model=Product)
def create_product(product: Product):
    try:
        return ProductService.create_product(product)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/product/{product_id}", response_model=Product)
def get_product(product_id: str):
    try:
        return ProductService.get_product_by_id(product_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.get("/product/{product_name}", response_model=Product)
def get_product_by_name(product_name: str):
    try:
        return ProductService.get_product_by_name(product_name)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/products", response_model=List[Product])
def get_all_products():
    try:
        return ProductService.get_all_products()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.put("/product/{product_id}", response_model=Product)
def update_product(product_id: str, product: Product):
    try:
        return ProductService.update_product(product_id, product)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.delete("/product/{product_id}", response_model=Product)
def delete_product(product_id: str):
    try:
        return ProductService.delete_product(product_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

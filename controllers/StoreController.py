from fastapi import APIRouter, HTTPException
from typing import List
from services.StoreService import StoreService
from models.store import Store

router = APIRouter()

@router.post("/store", response_model=Store)
def create_store(store: Store):
    try:
        return StoreService.create_store(store)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/store/{store_id}", response_model=Store)
def get_store(store_id: str):
    try:
        return StoreService.get_store_by_id(store_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/stores", response_model=List[Store])
def get_all_stores():
    try:
        return StoreService.get_all_stores()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.put("/store/{store_id}", response_model=Store)
def update_store(store_id: str, store: Store):
    try:
        return StoreService.update_store(store_id, store)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.delete("/store/{store_id}", response_model=Store)
def delete_store(store_id: str):
    try:
        return StoreService.delete_store(store_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

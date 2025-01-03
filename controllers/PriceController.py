from fastapi import APIRouter, HTTPException
from typing import List
from services.PriceService import PriceService
from models.price import Price

router = APIRouter()


@router.post("/price", response_model=Price)
def create_price(price: Price):
    try:
        return PriceService.create_price(price)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/price/{price_id}", response_model=Price)
def get_price(price_id: str):
    try:
        return PriceService.get_price_by_id(price_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/prices", response_model=List[Price])
def get_all_prices():
    try:
        return PriceService.get_all_prices()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/prices/store/{store_id}", response_model=List[Price])
def get_all_prices_by_store_id(store_id: str):
    try:
        return PriceService.get_all_prices_by_store_id(store_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.put("/price/{price_id}", response_model=Price)
def update_price(price_id: str, price: Price):
    try:
        return PriceService.update_price(price_id, price)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/price/{price_id}", response_model=Price)
def delete_price(price_id: str):
    try:
        return PriceService.delete_price(price_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

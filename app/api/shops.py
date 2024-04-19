from fastapi import APIRouter, HTTPException
from typing import List

from app.api.models import ShopOut, ShopIn
from app.api import db_manager

shops = APIRouter()

@shops.post('/', response_model=ShopOut, status_code=201)
async def create_shop(payload: ShopIn):
    shop_id = await db_manager.add_shop(payload)

    response = {
        'id': shop_id,
        **payload.dict()
    }

    return response


@shops.get('/', response_model=List[ShopOut])
async def get_shops():
    return await db_manager.get_all_shop()


@shops.get('/{id}/', response_model=ShopOut)
async def get_shop(id: int):
    shop = await db_manager.get_shop(id)
    if not shop:
        raise HTTPException(status_code=404, detail="Shop not found")
    return shop


@shops.delete('/{id}/', response_model=None)
async def delete_shop(id: int):
    shop = await db_manager.get_shop(id)
    if not shop:
        raise HTTPException(status_code=404, detail="Shop not found")
    return await db_manager.delete_shop(id)
from app.api.models import ShopIn, ShopOut
from app.api.db import shops, database


async def add_shop(payload: ShopIn):
    query = shops.insert().values(**payload.dict())
    return await database.execute(query=query)


async def get_all_shop():
    query = shops.select()
    return await database.fetch_all(query=query)


async def get_shop(id):
    query = shops.select().where(shops.c.id == id)
    return await database.fetch_one(query=query)


async def delete_shop(id: int):
    query = shops.delete().where(shops.c.id == id)
    return await database.execute(query=query)


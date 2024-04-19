from pydantic import BaseModel
from typing import List, Optional

class ShopIn(BaseModel):
    name: str
    phone: str
    city: str
    country: str

class ShopOut(ShopIn):
    id: int

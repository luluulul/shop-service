import pytest
from app.api.models import ShopIn, ShopOut

shops = ShopIn(
    name='Nike',
    phone='+79192034567',
    city='Moscow',
    country='Russia'
)


def test_create_reader(shops: ShopIn = shops):
    assert dict(shops) == {'name': shops.name,
                           'phone': shops.phone,
                           'city': shops.city,
                           'country': shops.country
                           }


def test_update_reader_age(shops: ShopIn = shops):
    shops_upd = ShopOut(
        name='Nike',
        phone='+79192034567',
        city='Moscow',
        country='Russia',
        id=1
    )
    assert dict(shops_upd) == {'name': shops.name,
                               'phone': shops.phone,
                               'city': shops.city,
                               'country': shops.country,
                               'id': shops_upd.id
                               }


def test_update_reader_city(shops: ShopIn = shops):
    shops_upd = ShopOut(
        name=shops.name,
        phone=shops.phone,
        city=shops.city,
        country=shops.country,
        id=1
    )
    assert dict(shops_upd) == {'name': shops.name,
                               'phone': shops.phone,
                               'city': shops.city,
                               'country': shops.country,
                               'id': shops_upd.id
                               }

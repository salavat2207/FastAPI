from app.database import SessionLocal
from app.booking.models import Bookings
from sqlalchemy import select



from fastapi.types import ModelNameMap
from sqlalchemy.util import monkeypatch_proxied_specials


class BaseDao:
    model = None

    @classmethod
    async def find_by_id(cls, model_id: int):
        async with SessionLocal() as session:
            query = select(cls.model).filter_by(id=model_id)
            result = await session.execute(query)
            return result.scalar_one_or_none()






    @classmethod
    async def find_one_or_none(cls, **filter_by):
        async with SessionLocal() as session:
            query = select(cls.model).filter_by(**filter_by)
            result = await session.execute(query)
            return result.scalar_one_or_none()


    @classmethod
    async def find_all(cls, **filter_by):
        async with SessionLocal() as session:
            query = select(cls.model).filter_by(**filter_by)
            result = await session.execute(query)
            return result.scalars().all()

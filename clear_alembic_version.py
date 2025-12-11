import asyncio
from sqlalchemy import text
from app.database import engine


async def clear_alembic_version():
    """Очищает таблицу alembic_version в базе данных."""
    async with engine.begin() as conn:
        await conn.execute(text("DROP TABLE IF EXISTS alembic_version"))
        print("✅ Таблица alembic_version успешно удалена!")


if __name__ == "__main__":
    asyncio.run(clear_alembic_version()) 
import asyncio

from sqlalchemy import text
from sqlalchemy.ext.asyncio import create_async_engine


engine = create_async_engine(URL, echo=True, future=True,)


async def main():
    async with engine.connect() as con:
        res = await con.execute(text("select 'hello world'"))
        print(res.all())


if __name__ == '__main__':
    asyncio.run(main)

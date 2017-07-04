from src.utils import common
from src.config import config
from asyncpg import create_pool
from sanic import Sanic
from sanic.response import json

if __name__ == "__main__":

    app = Sanic(__name__)

    @app.listener('before_server_start')
    async def register_db(app, _loop):
        app.pool = await create_pool(**config.db, loop=_loop, max_size=100)
        async with app.pool.acquire() as connection:
            await connection.execute('DROP TABLE IF EXISTS sanic_post')
            await connection.execute("""CREATE TABLE sanic_post (
                                    id serial primary key,
                                    content varchar(50),
                                    post_date timestamp
                                );""")
            for i in range(0, 1000):
                await connection.execute(f"""INSERT INTO sanic_post
                    (id, content, post_date) VALUES ({i}, {i}, now())""")

    @app.get('/')
    async def root_get(request):
        async with app.pool.acquire() as connection:
            results = await connection.fetch('SELECT * FROM sanic_post')
            return json({'posts': common.jsonify(results)})

    #The same as: host, port, debug, ssl, sock, workers, loop = config.server
    locals().update(config.server)
    app.run(host, port, debug, ssl, sock, workers, loop)

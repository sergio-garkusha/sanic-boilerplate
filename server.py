from os import environ as env
from sys import argv
from sanic import Sanic
from dotenv import load_dotenv, find_dotenv

print(bool(env.get("DEBUG")))

if __name__ == "__main__":
    load_dotenv(find_dotenv())

    host = env.get("HOST") or "localhost"
    port = int(env.get("PORT")) or 9080
    workers = int(env.get("WORKERS")) or 1
    debug = bool(env.get("DEBUG")) or False
    ssl = env.get("SSL") or None
    sock = env.get("SOCK") or None
    loop = env.get("LOOP") or None

    if len(argv) > 3:
        host = argv[2]
        port = argv[4]

    app = Sanic(__name__)

    app.run(host, port, debug, ssl, sock, workers, loop)

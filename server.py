from sys import argv
from sanic import Sanic
# print (sanic.__file__)

if __name__ == "__main__":
    host = "127.0.0.1"
    port = 9080

    if len(argv) > 3:
        host = argv[2]
        port = argv[4]

    app = Sanic()
    app.run(host, port)

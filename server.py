from sanic import Sanic

app = Sanic()

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=9080)

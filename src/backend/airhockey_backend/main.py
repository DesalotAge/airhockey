from aiohttp import web


async def index(request):
    return web.Response(text="Hello, world")


async def get_all_users(request):
    return web.Response(text="first, second")


async def register_user(request):
    return web.Response(text=(await request.text()))


app = web.Application()

app.add_routes([
    web.get("/", index),
    web.get("/users/", get_all_users),
    web.post("/users/", register_user),
])


if __name__ == "__main__":
    web.run_app(app)

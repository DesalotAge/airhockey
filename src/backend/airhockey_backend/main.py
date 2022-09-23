from aiohttp import web
from api.users import URLS
from api.utils import RouterRegistryService


async def index(request):
    return web.Response(text="Hello, world")


app = web.Application()

rrs = RouterRegistryService(app)
rrs.register_routes(URLS)


app.add_routes([
    web.get("/", index),
])


if __name__ == "__main__":
    web.run_app(app)

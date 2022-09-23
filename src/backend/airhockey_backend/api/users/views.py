from aiohttp import web


async def get_all_users(request):
    return web.Response(text="first, second")


async def register_user(request):
    return web.Response(text=(await request.text()))

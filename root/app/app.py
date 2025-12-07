from aiohttp import web

async def init_app() -> web.Application:
    app = web.Application()
    app.add_routes()
    return app
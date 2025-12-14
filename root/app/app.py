from aiohttp import web

from root.app.api.router import routes_table

async def init_app() -> web.Application:
    app = web.Application()
    app.add_routes(routes_table)
    return app
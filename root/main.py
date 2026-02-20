from aiohttp import web

from root.presentation.routes import routes
from root.infrastructure.di.container import DIContainer
from root.config import SERVER_CONFIG, DATABASE_CONFIG

async def on_startup(app):
    di_container = DIContainer()
    di_container.init_resources(db_config=DATABASE_CONFIG)
    app["di_container"] = di_container

server = web.Application()
server.add_routes(routes)
server.on_startup.append(on_startup)

def start_server() -> None:
    web.run_app(server, **SERVER_CONFIG)
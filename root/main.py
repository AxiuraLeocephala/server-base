from aiohttp import web

from root.presentation.routes import routes
from root.infrastructure.di.container import DIContainer

async def on_startup(app):
    di_container = DIContainer()
    di_container.init_resources(db_config={
        "host": "127.0.0.1",
        "port": 3306,
        "user": "root",
        "password": "root",
        "database": "hackaton_2.0"
    })
    app["di_container"] = di_container

server = web.Application()
server.add_routes(routes)
server.on_startup.append(on_startup)

def start_server() -> None:
    web.run_app(server, host="127.0.0.1", port=8080)
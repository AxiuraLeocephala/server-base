from aiohttp import web

from root.presentation.routes import routes 

server = web.Application()
server.add_routes(routes)

def start_server() -> None:
    web.run_app(server, host="127.0.0.1", port=8080)
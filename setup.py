import asyncio

from aiohttp import web

from root.app import init_app
from setting import SERVER_CONFIG

def setup() -> None:
    app = asyncio.run(init_app())
    web.run_app(
        app, 
        host=SERVER_CONFIG["host"], 
        port=SERVER_CONFIG["port"]
    )

if __name__ == "__main__":
    setup()
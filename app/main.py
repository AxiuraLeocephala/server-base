from aiohttp import web

async def on_startup():
    pass

async def on_shutdown():
    pass

def setup_main():
    app = web.Application()
    
    app.on_startup(on_startup)
    app.on_shutdown(on_shutdown)
    
    web.run_app(
        app,
        host="127.0.0.1",
        port=3000,
    )


if __name__ == "main":
    setup_main()
from aiohttp import web

async def register_team_handler(request: web.Request) -> web.Response:
    data = await request.json()
    print(data)
    return web.Response(text="sucsessful", status=200)

async def register_athlete_handler(request: web.Request) -> web.Response:
    data = await request.json()
    print(data)
    return web.Response(text="sucsessful", status=200)
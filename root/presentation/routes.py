from aiohttp import web

from root.presentation.http.handlers import register_team_handler, register_athlete_handler

routes = web.RouteTableDef()

@routes.post('/register_team')
async def register_team(request: web.Request) -> web.Response:
    return await register_team_handler(request)

@routes.post("/register_athlete")
async def register_athlete(request: web.Request) -> web.Response:
    return await register_athlete_handler(request)
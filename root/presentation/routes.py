from aiohttp import web

from root.presentation.http.handlers import *

routes = web.RouteTableDef()

@routes.post('/create_competition')
async def create_competition(request: web.Request) -> web.Response:
    return await create_competition_handler(request)

@routes.post('/register_team')
async def register_team(request: web.Request) -> web.Response:
    return await register_team_handler(request)

@routes.get('/get_team')
async def get_team(request: web.Request) -> web.Response:
    return await get_team_handler(request)
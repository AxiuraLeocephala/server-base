from aiohttp import web

from root.presentation.http.handlers import register_team_handler

routes = web.RouteTableDef()

@routes.post('/register_team')
async def register_team(request: web.Request) -> web.Response:
    return await register_team_handler(request)
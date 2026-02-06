from aiohttp import web

from root.application.use_cases import RegisterTeamWithMembers

async def register_team_handler(request: web.Request) -> web.Response:
    data = await request.json()
    register_team = RegisterTeamWithMembers()
    register_team.execute(
        name=data["team"]["name"],
        region=data["team"]["region"],
        organization=data["team"]["organization"]
    )
    return web.Response(text="sucsessful", status=200)

async def register_athlete_handler(request: web.Request) -> web.Response:
    data = await request.json()
    print(data)
    return web.Response(text="sucsessful", status=200)
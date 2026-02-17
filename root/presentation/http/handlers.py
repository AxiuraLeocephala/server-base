import logging

from aiohttp import web
from aiohttp.web_response import json_response

async def register_team_handler(request: web.Request) -> web.Response:
    data = await request.json()
    di_container = request.app["di_container"]
    register_team = di_container.register_team_use_case()
    
    try:
        await register_team.execute(
            name=data["team"]["name"],
            region=data["team"]["region"],
            organization=data["team"]["organization"],
            members=data["team"]["members"]
        )
    except Exception as e:
        logging.exception(f"failed to register team{e}")
        return web.Response(
            body={
                "message": "failed to register team"
            }, 
            status=400
        )
    
    return web.Response(status=200)

async def get_team_handler(request: web.Request) -> web.Response:
    data = await request.json()
    di_container = request.app["di_container"]
    get_team = di_container.get_team_use_case()

    try:
        teams = await get_team.execute(id=data["id"])
    except Exception as e:
        logging.exception(f"failed to get team: {e}")
        return web.Response(
            body={
                "message": "failed to get team", 
            },
            status=400
        )
    
    print(teams)
    
    # return json_response({"data": teams}, status=200)
    return web.Response(status=200)
import logging
import json

from aiohttp import web
from aiohttp.web_response import json_response

from root.presentation.utils import CustomJSONEncoder

async def create_competition_handler(request: web.Request) -> web.Response:
    data = await request.json()
    di_container = request.app["di_container"]
    create_competition = di_container.create_competition_use_case()

    try:
        await create_competition.execute(
            name=data["competition"]["name"],
            start_date_time=data["competition"]["start_date_time"],
            end_date_time=data["competition"]["end_date_time"],
            location=data["competition"]["location"],
            organizer=data["competition"]["organizer"]
        )

        return web.Response(status=200)
    except Exception as e:
        logging.exception(f"failed to create competition: {e}")
        return json_response(
            data={
                "message": "failed to register team"
            },
            status=400
        )

async def get_competition_hanler(request: web.Request) -> web.Response:
    data = await request.json()
    di_container = request.app["di_container"]
    get_competitions = di_container.get_competitions_use_case()

    try:
        competitions = await get_competitions.execute()

        if competitions: 
            for i, competition in enumerate(competitions):
                competition[i] = json.dumps(competitions, cls=CustomJSONEncoder, ensure_ascii=False)

        return json_response(data={"competitions": competitions}, status=200)
    except Exception as e:
        logging.exception(f"failed to get competitions: {e}")
        return json_response(
            data={
                "message": "failed to get competitions"
            },
            status=400
        )

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

        return web.Response(status=200)
    except Exception as e:
        logging.exception(f"failed to register team{e}")
        return json_response(
            data={
                "message": "failed to register team"
            }, 
            status=400
        )

async def get_team_handler(request: web.Request) -> web.Response:
    data = await request.json()
    di_container = request.app["di_container"]
    get_team = di_container.get_team_use_case()

    try:
        teams = await get_team.execute(id=data["id"])
        if teams:
            for i, team in enumerate(teams):
                teams[i] = json.dumps(team, cls=CustomJSONEncoder, ensure_ascii=False)
        
        return json_response(data={"teams": teams}, status=200)
    except Exception as e:
        logging.exception(f"failed to get team: {e}")
        return json_response(
            data={
                "message": "failed to get team"
            },
            status=400
        )
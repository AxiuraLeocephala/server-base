import logging

from aiohttp import web

async def register_team_handler(request: web.Request) -> web.Response:
    data = await request.json()
    di_container = request.app["di_container"]
    use_case = di_container.register_team_use_case()
    try:
        await use_case.execute(
            name=data["team"]["name"],
            region=data["team"]["region"],
            organization=data["team"]["organization"],
            members=data["team"]["members"]
        )
    except Exception as e:
        logging.error(f"Failed to register team: {e}")
        return web.Response(text="Failed to register team", status=400)
    return web.Response(text="sucsessful", status=200)
from aiohttp import web

routes_table = [
    web.get("participant_rating", get_participant_rating)
]
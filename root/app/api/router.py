from aiohttp import web
from root.app.api.v1 import *

routes_table = [
    web.get("participant_rating", get_participants_rating)
]
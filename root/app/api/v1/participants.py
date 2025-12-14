from aiohttp import web
from aiohttp.web import json_response

def get_participants_rating(request: web.Request) -> web.Response:
    try:
        rating = 1
        
        return json_response(
            data={
                "sucsessful": True,
                "rating": rating
            }
        )
    except Exception as error:
        return json_response(
            data={
                "sucsessful": False,
                "message": "Возникла ошибка при получении рейтинга участников",
            },
            status=400
        )
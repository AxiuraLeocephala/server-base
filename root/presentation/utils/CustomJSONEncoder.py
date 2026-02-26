from json import JSONEncoder
from typing import Any

from root.domain.entities import Team, Competition

class CustomJSONEncoder(JSONEncoder):
    def default(self, obj: Any):
        if isinstance(obj, Team):
            obj.members = [vars(athlete) for athlete in obj.members]
            return vars(obj)
        elif isinstance(obj, Competition):
            stri = obj.start_date_time
            print(stri)
            return vars(obj)
        else:
            super().default(obj)
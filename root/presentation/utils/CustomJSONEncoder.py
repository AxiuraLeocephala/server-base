from json import JSONEncoder
from typing import Any

from root.domain.entities import Team

class CustomJSONEncoder(JSONEncoder):
    def default(self, obj: Any):
        if isinstance(obj, Team):
            obj.members = [vars(athlete) for athlete in obj.members]
            return vars(obj)
        
        super().default(obj)
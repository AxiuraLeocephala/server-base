from json import JSONEncoder

from root.domain.entities import Athlete, Team

class CustomJSONEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Team):
            obj.members = [vars(athlete) for athlete in obj.members]
            return vars(obj)
        
        super().default(obj)
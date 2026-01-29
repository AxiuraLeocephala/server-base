from typing import Dict, Tuple, Union

class Team:
    def __init__(self, name: str, team_members: Union[Tuple, Dict]):
        self.name = name
        self.team_members = team_members
from typing import List, Tuple, Union

class Team:
    def __init__(
            self, 
            name: str, region: str, organization: str, 
            team_members: Union[Tuple, List, None]
        ):
        self.name = name
        self.region = region
        self.organization = organization
        self.team_members = team_members
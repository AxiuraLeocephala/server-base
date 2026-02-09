from typing import List, Tuple, Union

class Team:
    def __init__(
            self, name: str, region: str, organization: str,
            id: Union[int, None] = None, members: Union[Tuple, List, None] = [], 
        ):
        self.id: Union[int, None] = id
        self.name: str = name
        self.region: str = region
        self.organization: str = organization
        self.members: Union[Tuple, List, None] = members
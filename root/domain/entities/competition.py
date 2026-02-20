from typing import Union

from root.domain.value_objects import mDateTime, CompetitionStatus

class Competition:
    def __init__(
            self, 
            name: str, start_date_time: mDateTime, end_date_time: mDateTime,
            location: str, organizer: str, id: Union[int, None] = None, 
            status: Union[CompetitionStatus, None] = None 
            ):
        self.id = id
        self.name = name
        self.start_date_time = start_date_time
        self.end_date_time = end_date_time
        self.location = location
        self.status = status
        self.organizer = organizer
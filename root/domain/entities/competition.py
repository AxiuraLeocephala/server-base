from root.domain.value_objects import mDateTime, CompetitionStatus

class Competition:
    def __init__(
            self, 
            id: int, name: str, start_datetime: mDateTime, end_datetime: mDateTime,
            location: str, status: CompetitionStatus, organizer: str
            ):
        self.id = id
        self.name = name
        self.start_datetime = start_datetime
        self.end_datetime = end_datetime
        self.location = location
        self.status = status
        self.organizer = organizer

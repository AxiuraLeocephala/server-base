from root.domain.value_objects import DisciplineType, PolyathlonType

class Discipline:
    def __init__(
            self,
            id: int, name: str, type: DisciplineType, polyathlon_type: PolyathlonType
        ):
        self.id = id
        self.name = name
        self.type = type
        self.polyathlon_type = polyathlon_type
from root.domain.value_objects import Gender

class AgeGroup:
    def __init__(
            self, 
            id: int, name: str, min_age: int, max_age: int, gender: Gender, 
            ):
        self.id = id
        self.name = name
        self.min_age = min_age
        self.max_age = max_age
        self.gender = gender
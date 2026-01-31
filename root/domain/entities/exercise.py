from root.domain.entities import AgeGroup, Discipline
from root.domain.value_objects import MeansurementType, MeansurementUnit

class Exercise:
    def __init__(
            self,
            id: int, name: str, discipline: Discipline, age_group: AgeGroup,
            meansurement_type: MeansurementType, meansurement_unit: MeansurementUnit
        ):
        self.id = id
        self.name = name
        self.discipline = discipline
        self.age_group = age_group
        self.meansurement_type = meansurement_type
        self.meansurement_unit = meansurement_unit
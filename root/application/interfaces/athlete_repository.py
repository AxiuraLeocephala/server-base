from abc import ABC, abstractmethod
from typing import Union

from root.domain.entities import Athlete, Competition, AgeGroup, Exercise

class AthleteRepository(ABC):
    @abstractmethod
    async def create(self, athlete: Athlete) -> None: pass

    @abstractmethod
    async def get_by_id(self, id: int) -> Union[Athlete, None]: pass

    @abstractmethod
    async def register(
        self, 
        competition: Competition, athlete: Athlete, age_group: AgeGroup
    ) -> None: pass

    @abstractmethod
    async def perform_exercise(
        self,
        athlete: Athlete, exercise: Exercise, competition: Competition, 
        raw_result: str
    ) -> None: pass

    @abstractmethod
    async def save(self, athlete: Athlete) -> None: pass
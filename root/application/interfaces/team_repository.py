from abc import ABC, abstractmethod
from typing import Union

from root.domain.entities import Athlete, Competition, Exercise, Team

class TeamRepository(ABC):
    @abstractmethod
    async def get_by_id(self, id: int) -> Union[Team, None]: pass

    @abstractmethod
    async def add_member(self, athlete: Athlete) -> None: pass

    @abstractmethod
    async def perform_exercise(
        self,
        team: Team, exercise: Exercise, competition: Competition, raw_result: str
    ) -> None: pass

    @abstractmethod
    async def save(self, team: Team) -> None: pass
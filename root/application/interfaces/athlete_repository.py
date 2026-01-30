from abc import ABC, abstractmethod
from typing import Union

from root.domain.entities.athlete import Athlete

class AthleteRepository(ABC):
    @abstractmethod
    async def get_by_id(self, id: int) -> Union[Athlete, None]: pass

    @abstractmethod
    async def save(self, athlete: Athlete) -> None: pass
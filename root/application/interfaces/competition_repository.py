from abc import ABC, abstractmethod
from typing import List, Union

from root.domain.entities import Competition

class CompetitionRepository(ABC):
    @abstractmethod
    async def create(self, competition: Competition) -> None: pass

    @abstractmethod
    async def get_all(self) -> Union[List[Competition], None]: pass
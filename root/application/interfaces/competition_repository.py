from abc import ABC, abstractmethod

from root.domain.entities import Competition

class CompetitionRepository(ABC):
    @abstractmethod
    def create(self, competition: Competition) -> None: pass
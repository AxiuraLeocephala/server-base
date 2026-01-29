from abc import ABC, abstractmethod
from typing import Union

from root.domain.entities.participant import Partisipant

class ParticipantRepository(ABC):
    @abstractmethod
    async def get_by_id(self, participant_id: int) -> Union[Partisipant, None]: pass

    @abstractmethod
    async def save(self, participant: Partisipant) -> None: pass
from abc import ABC, abstractmethod

class ParticipantRepository(ABC):
    @abstractmethod
    def get_all(self): pass
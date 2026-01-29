from abc import ABC, abstractmethod
from typing import Union, Dict, Tuple

class DB_Interface(ABC):
    @abstractmethod
    async def execute(
        self, 
        sql: str, params: Union[Tuple, Dict] = None
    ) -> None: pass

    @abstractmethod
    async def query(
        self, 
        sql: str, params: Union[Tuple, Dict] = None
    ) -> Union[Tuple, Dict, None]: pass
    
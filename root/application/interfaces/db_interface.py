from abc import ABC, abstractmethod
from typing import Union, Dict, List, Tuple

class DBInterface(ABC):
    @abstractmethod
    async def execute(
        self, 
        sql: str, params: Union[Tuple, Dict, None] = None
    ) -> Union[int, None]: pass

    @abstractmethod
    async def query(
        self, 
        sql: str, params: Union[Tuple, Dict, None] = None
    ) -> List: pass
    
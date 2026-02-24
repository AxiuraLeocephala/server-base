from typing import Union, List

from root.infrastructure.db.repositories import MySQLCompetitionRepository
from root.domain.entities import Competition

class GetCompetitions:
    def __init__(self, competition_repository: MySQLCompetitionRepository):
        self.__competitions_repository = competition_repository

    async def execute(self) -> Union[List[Competition], None]:
        competitions = await self.__competitions_repository.get_all()

        if not competitions: return None

        return competitions


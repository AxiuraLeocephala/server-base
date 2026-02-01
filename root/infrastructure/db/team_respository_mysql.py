from typing import Union

from root.application.interfaces import TeamRepository
from root.domain.entities import Team
from root.infrastructure.db.mysql import MySQL

class MySQLTeamRepository(TeamRepository):
    def __init__(self, mysql: MySQL):
        self.__mysql = mysql

    async def get_by_id(self, id: int) -> Union[Team, None]:
        team_data = await self.__mysql.query(
            "SELECT * FROM teams WHERE ID=%d",
            (id,)
        )

        if not team_data: return None

        return Team(
            id=team_data["ID"],
            name=team_data["name"],
            region=team_data["region"],
            organization=team_data["organization"]
            
        )
from typing import Union

from root.application.interfaces import TeamRepository
from root.domain.entities import Athlete, Competition, Exercise, Team
from root.infrastructure.db.mysql import MySQL

class MySQLTeamRepository(TeamRepository):
    def __init__(self, mysql: MySQL):
        self.__mysql = mysql

    async def create(self, team: Team) -> None:
        team_id = await self.__mysql.execute(
            "INSERT INTO team " \
            "(name, region, organization) " \
            "VALUE (%s, %s, %s);"
            "SELECT SCOPE_IDENTITY();",
            (team.name, team.region, team.organization)
        )

        team.id = team_id

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

    async def add_member(self, team: Team, athlete: Athlete) -> None:
        await self.__mysql.execute(
            "UPDATE athletes SET team_id=%d WHERE ID=%d",
            (team.id, athlete.id)
        )

    async def perform_exercise(
            self, 
            team: Team, exercise: Exercise, competition: Competition, 
            raw_result: str
        ) -> None:
        await self.__mysql.execute(
            "INSERT INTO team_performances "
            "(team_id, exercise_id, competition_id, raw_result) " \
            "VALUE (%d, %d, %d, %s)",
            (team.id, exercise.id, competition.id, raw_result)
        )

    async def save(self, team: Team) -> None:
        await self.__mysql.execute(
            "UPDATE teams SET name=%s, region=%s, organization=%s WHERE ID=%d",
            (team.name, team.region, team.organization, team.id)
        )
        
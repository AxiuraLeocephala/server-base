from root.application.interfaces import CompetitionRepository
from root.domain.entities import Competition
from root.infrastructure.db.mysql import MySQL

class MySQLCompetitionRepository(CompetitionRepository):
    def __init__(self, mysql: MySQL):
        self.__mysql = mysql

    async def create(self, competition: Competition) -> None:
        competition_id = await self.__mysql.execute(
            "INSERT INTO competitions " \
            "(name, start_date_time, end_date_time, " \
            "location, status, organizer) " \
            "VALUES (%s, %s, %s, %s, %s, %s);",
            (competition.name, competition.start_date_time, competition.end_date_time,
             competition.location, competition.status, competition.organizer)
        )

        competition.id = competition_id

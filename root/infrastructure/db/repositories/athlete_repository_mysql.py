from typing import Union

from root.application.interfaces import AthleteRepository
from root.infrastructure.db.mysql import MySQL
from root.domain.entities import Athlete, AgeGroup, Competition, Team 

class MySQLAthleteRepository(AthleteRepository):
    def __init__(self, mysql: MySQL):
        self.__mysql = mysql

    async def create(self, athlete: Athlete) -> None:
        await self.__mysql.execute(
            "INSERT INTO athletes " \
            "(team_id, first_name, last_name, gender, birth_date, sport_rank)" \
            "VALUE (%s, %s, %s, %s, %s, %s)",
            (athlete.team_id, athlete.first_name, athlete.last_name, 
             athlete.gender, athlete.birth_date, athlete.sport_rank)
        )

    async def get_by_id(self, id: int) -> Union[Athlete, None]:
        athlete_data = await self.__mysql.query(
            "SELECT * FROM athletes WHERE id=%d",
            (id,)
        )

        if not athlete_data: return None

        return Athlete(
            id=athlete_data['id'],
            team_id=athlete_data['team_id'],
            first_name=athlete_data['first_name'],
            last_name=athlete_data['last_name'],
            gender=athlete_data['gender'],
            birth_date=athlete_data['birth_date'],
            sport_rank=athlete_data['sport_rank']
        )
    
    async def register(
            self, 
            competition: Competition, athlete: Athlete, age_group: AgeGroup
        ) -> None:
        await self.__mysql.execute(
            "INSERT INTO registrations "
            "(competition_id, athlete_id, age_group_id) " \
            "VALUES (%d, %d, %d)",
            (competition.id, athlete.id, age_group.id)
        )

    async def add_to_team(self, team: Team, athlete: Athlete) -> None:
        await self.__mysql.execute(
            "UPDATE athletes SET team_id=%d WHERE ID=%d",
            (team.id, athlete.id)
        )

    async def perform_exercise(self, athlete: Athlete, exercise, competition, raw_result):
        await self.__mysql.execute(
            "INSERT INTO performances " \
            "(athlete_id, exercise_id, competition_id, raw_result) " \
            "VALUES (%d, %d, %d, %s)",
            (athlete.id, exercise.id, competition.id, raw_result)
        )

    async def save(self, athlete: Athlete) -> None:
        await self.__mysql.execute(
            "UPDATE athletes " \
            "SET team_id=%d, first_name=%s, last_name=%s, " \
            "gender=%s, birth_date=%s, sport_rank=%s " \
            "WHERE id=%d",
            (athlete.first_name, athlete.last_name, athlete.gender, 
             athlete.birth_date, athlete.sport_rank, athlete.id)
        )
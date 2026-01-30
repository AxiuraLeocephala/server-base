from typing import Union

from root.application.interfaces.athlete_repository import AthleteRepository
from root.infrastructure.db.mysql import MySQL
from root.domain.entities.athlete import Athlete

class MySQLAthleteRepository(AthleteRepository):
    def __init__(self, mysql: MySQL):
        self.__mysql = mysql

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
    
    async def save(self, athlete: Athlete) -> None:
        await self.__mysql.execute(
            "UPDATE athletes " \
            "SET team_id=%d, first_name=%s, last_name=%s, gender=%s, birth_date=%s, sport_rank=%s " \
            "WHERE id=%d",
            (athlete.first_name, athlete.last_name, athlete.gender, athlete.birth_date, athlete.sport_rank, athlete.id)
        )
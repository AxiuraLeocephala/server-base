from root.application.interfaces import AthleteRepository
from root.domain.entities import Athlete, Team
from root.domain.value_objects import Gender, mDate, SportRank

class RegisterAthlete:
    def __init__(self, athlete_repository: AthleteRepository):
        self.__athlete_repository = athlete_repository

    async def execute(
            self, 
            team: Team, first_name: str, last_name: str, 
            gender: Gender, birth_date: mDate, sport_rank: SportRank
        ):
        user = Athlete(
            team_id=team.id,
            first_name=first_name,
            last_name=last_name,
            gender=gender,
            birth_date=birth_date,
            sport_rank=sport_rank
        )

        
        
        await self.__athlete_repository.save(user)

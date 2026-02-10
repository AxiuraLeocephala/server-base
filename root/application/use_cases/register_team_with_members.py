from root.application.interfaces import TeamRepository, AthleteRepository
from root.domain.entities import Athlete, Team

class RegisterTeamWithMembers:
    def __init__(self, team_repository: TeamRepository, athlete_repository: AthleteRepository):
        self.__team_repository = team_repository
        self.__athlete_repository = athlete_repository

    async def execute(self, name, region, organization, members):
        # TODO сделать транзакцию в MySQL
        team = Team(
            name=name,
            region=region,
            organization=organization,
        )

        await self.__team_repository.create(team)

        for member in members: 
            athlete = Athlete(
                team_id=team.id,
                first_name=member["first_name"],
                last_name=member["last_name"],
                gender=member["gender"],
                birth_date=member["birth_date"],
                sport_rank=member["sport_rank"]
            )

            await self.__athlete_repository.create(athlete)

            team.members.append(athlete)
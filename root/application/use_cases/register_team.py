from root.application.interfaces import TeamRepository
from root.domain.entities import Team

class RegisterTeam:
    def __init__(self, team_repository: TeamRepository):
        self.__team_repository = team_repository

    
    async def execute(self, name: str, region: str, organization: str):
        team = Team(
            name=name,
            region=region,
            organization=organization
        )

        await self.__team_repository.create(team)

        return team
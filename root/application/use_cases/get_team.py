from typing import Union, Literal, List
import json

from root.application.interfaces import AthleteRepository, TeamRepository
from root.domain.entities import Team

class GetTeam:
    def __init__(self, team_repository: TeamRepository, athlete_repository: AthleteRepository):
        self.__team_repository = team_repository
        self.__athlete_repository = athlete_repository

    async def execute(self, id=Union[Literal["*"], int, List[int]]) -> Union[Team, List[Team], None]:
        if id == "*":
            teams = await self.__team_repository.get_all()

            if not teams: return None

            for team in teams:
                team.members = await self.__athlete_repository.get_by_team_id(team.id)

            return teams
        elif isinstance(id, int):
            team = await self.__team_repository.get_by_id(id)

            if not team: return None
            
            team.members = await self.__athlete_repository.get_by_team_id(team.id)
            
            return team
        else:
            teams = []

            for team_id in id:
                team = await self.__team_repository.get_by_id(team_id)
                if not team: continue
                team.members = await self.__athlete_repository.get_by_team_id(team.id)
                teams.append(team)

            return teams

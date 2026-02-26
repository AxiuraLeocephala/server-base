from typing import Dict

from root.application.use_cases import *
from root.infrastructure.db.repositories import *
from root.infrastructure.db.mysql import MySQL

class DIContainer:
    def __init__(self):
        self.__mysql: MySQL
        self.__competition_repository: MySQLCompetitionRepository
        self.__athlete_repository: MySQLAthleteRepository
        self.__team_repository: MySQLTeamRepository

    def init_resources(self, db_config: Dict) -> None:
        self.__mysql = MySQL(db_config)
        self.__competition_repository = MySQLCompetitionRepository(self.__mysql)
        self.__athlete_repository = MySQLAthleteRepository(self.__mysql)
        self.__team_repository = MySQLTeamRepository(self.__mysql)

    def create_competition_use_case(self) -> CreateCompetition:
        return CreateCompetition(
            competition_repository=self.__competition_repository
        )
    
    def get_competitions_use_case(self) -> GetCompetitions:
        return GetCompetitions(
            competition_repository=self.__competition_repository
        )

    def register_team_use_case(self) -> RegisterTeamWithMembers:
        return RegisterTeamWithMembers(
            athlete_repository=self.__athlete_repository,
            team_repository=self.__team_repository
        )
    
    def get_team_use_case(self) -> GetTeam:
        return GetTeam(
            team_repository=self.__team_repository,
            athlete_repository=self.__athlete_repository
        )
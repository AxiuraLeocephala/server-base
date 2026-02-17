from root.application.use_cases import RegisterTeamWithMembers, GetTeam
from root.infrastructure.db.repositories import MySQLAthleteRepository, MySQLTeamRepository
from root.infrastructure.db.mysql import MySQL

class DIContainer:
    def __init__(self):
        self.__mysql = None
        self.__athlete_repository = None
        self.__team_repository = None

    def init_resources(self, db_config) -> None:
        self.__mysql = MySQL(db_config)
        self.__athlete_repository = MySQLAthleteRepository(self.__mysql)
        self.__team_repository = MySQLTeamRepository(self.__mysql)

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
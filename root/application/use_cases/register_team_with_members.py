from root.application.interfaces import TeamRepository, AthleteRepository

class RegisterTeamWithMembers:
    def __init__(self, team_repository: TeamRepository, athlete_repository: AthleteRepository):
        self.__team_repository = team_repository
        self.__athlete_repository = athlete_repository

    def execute(self, name, region, organization, members):
        team = self.__team_repository.create(name=name, region=region, organization=organization)
        print(team)
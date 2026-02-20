from root.application.interfaces import CompetitionRepository
from root.domain.entities import Competition
from root.domain.value_objects import mDateTime

class CreateCompetition:
    def __init__(self, competition_repository: CompetitionRepository):
        self.__competition_repository = competition_repository

    async def execute(
            self, 
            name: str, start_date_time: mDateTime, end_date_time: mDateTime,
            location: str, organizer: str
    ) -> None: 
        competition = Competition(
            name=name,
            start_date_time=start_date_time,
            end_date_time=end_date_time,
            location=location,
            status="planned",
            organizer=organizer
        )

        await self.__competition_repository.create(competition)

        return Competition
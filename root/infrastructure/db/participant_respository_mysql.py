from typing import Union

from root.application.interfaces.participant_repository import ParticipantRepository
from root.infrastructure.db.mysql import MySQL
from root.domain.entities.participant import Participant

class MySQLParticipantRepository(ParticipantRepository):
    def __init__(self, mysql: MySQL):
        self.__mysql = mysql

    async def get_by_id(self, participant_id: int) -> Union[Participant, None]:
        participant_data = await self.__mysql.query(
            "SELECT id, first_name, second_name FROM participants WHERE id=%s",
            (participant_id,)
        )

        if not participant_data: return None

        return Participant(
            id=participant_data["id"],
            first_name=participant_data["first_name"],
            second_name=participant_data["second_name"]
        )
    
    async def save(self, participant: Participant) -> None:
        await self.__mysql.execute(
            "UPDATE participants SET first_name=%s, second_name=%s",
            (participant.first_name, participant.second_name)
        )
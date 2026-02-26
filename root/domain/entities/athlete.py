from root.domain.value_objects import Gender, MySQLDate, SportRank

class Athlete:
    def __init__(
            self, 
            id: int, team_id: int, first_name: str, last_name: str,
            gender: Gender, birth_date: MySQLDate, sport_rank: SportRank
            ):
        self.id: int = id
        self.team_id: int = team_id
        self.first_name: str = first_name
        self.last_name: str = last_name
        self.gender: Gender = gender
        self.birth_date: MySQLDate = birth_date
        self.sport_rank: SportRank = sport_rank
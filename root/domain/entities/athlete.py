from root.domain.value_objects import Gender, mDate, SportRank

class Athlete:
    def __init__(
            self, 
            team_id: int, first_name: str, last_name: str,
            gender: Gender, birth_date: mDate, sport_rank: SportRank
            ):
        self.team_id = team_id
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.birth_date = birth_date
        self.sport_rank = sport_rank
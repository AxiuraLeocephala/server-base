from enum import Enum

class SportRank(Enum):
    HONORED_MASTER_OF_SPORT_RUSSIA = "заслуженный мастер спорта России"
    MASTER_OF_SPORT_RUSSIA_OF_INTERNATIONAL_CLASS = "мастер спорта России международного класса"
    MASTER_OF_SPORT_RUSSIA = "мастер спорта России"
    CANDIDATE_MASTER_OF_SPORT_RUSSIA = "КМС"
    FIRST_SPORT_DEGREE = "1 спортивный разряд"
    SECOND_SPORT_DEGREE = "2 спортивный разряд"
    THIRD_SPORT_DEGREE = "3 спортивный разряд"
    FIRST_YOUTH_DEGREE = "1 юнощеский разряд"
    SECOND_YOUTH_DEGREE = "2 юнощеский разряд"
    THIRD_YOUTH_DEGREE = "3 юнощеский разряд"
    NO_RANK = "Без разряда"
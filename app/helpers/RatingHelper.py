from app.constants import rating


class RatingHelper:
    @staticmethod
    def int_to_short(rating_int: int) -> str:
        return rating.short_map.get(rating_int, 'UNK')

    @staticmethod
    def int_to_long(rating_int: int) -> str:
        return rating.long_map.get(rating_int, 'Unknown')

from datetime import datetime


class Round:

    def __init__(self, round_number):
        """
        Initialize a Round instance.

        Args:
        - round_number
        """
        self.round_number = round_number
        self.matches = []
        self.start_date = None
        self.end_date = None

    def add_match(self, match):
        """
        Add a match to the round.

        Args:
        - match (Match): The match to add to the round.
        """
        self.matches.append(match)

    def start_round(self):
        """
        Set the start date of the round to the current date and time.

        Returns:
        datetime: The start date of the round.
        """
        self.start_date = datetime.now()
        return self.start_date

    def end_round(self):
        """
        Set the end date of the round to the current date and time.

        Returns:
        datetime: The end date of the round.
        """
        self.end_date = datetime.now()
        return self.end_date

    def to_dict(self):
        return {
            "round_number": self.round_number,
            "matches": [{"match_id": match.id_match} for match in self.matches]
        }

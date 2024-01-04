from models.round import Round


class Tournament:

    json_file = "data/players.json"

    def __init__(self, name, place=None, start_date=None, end_date=None, rounds=None):
        """
        Initialize a Tournament instance.

        Args:
        - name: The name of the tournament.
        - place: The place where the tournament takes place (default is None).
        - start_date: The start date of the tournament in the format 'YYYY-MM-DD' (default is None).
        - end_date: The end date of the tournament in the format 'YYYY-MM-DD' (default is None).
        """
        self.name = name
        self.place = place
        self.start_date = start_date
        self.end_date = end_date
        self.current_round = 0
        self.nbr_of_round = 4
        self.description = ""
        self.rounds = [Round(i + 1) for i in range(self.nbr_of_round)]
        self.players = []
        self.matches = []

    def to_dict(self):
        """
        Convert Tournament object to a dictionary.

        Returns:
        dict: Dictionary representation of the Tournament object.
        """
        return {
            "name": self.name,
            "place": self.place,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "current_round": self.current_round,
            "players": [{"chess_id": player.chess_id, "points": player.points} for player in self.players],
            "rounds": [round.to_dict() for round in self.rounds]
        }

    def add_match(self, match, round_number):
        """
        Add a match to the tournament.

        Args:
        - match (Match): The match to add.
        """
        match.tournament = self  # Set the tournament of the match
        self.matches.append(match)
        self.rounds[round_number-1].add_match(match)

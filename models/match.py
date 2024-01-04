import uuid


class Match:

    def __init__(self, player1, player2, winner=None):
        """
        Initialize a Match instance.

        Args:
        - player1 (Player): The first player.
        - player2 (Player): The second player.
        - winner (Player): The winner of the match (default is None).
        """
        self.player1 = player1
        self.player2 = player2
        self.winner = winner
        self.id_match = str(uuid.uuid4())

    def to_dict(self):
        """
        Convert Match object to a dictionary.

        Returns:
        dict: Dictionary representation of the Match object.
        """
        return {
            "match_id": self.id_match,
            "player 1": {"chess_id": self.player1.chess_id},
            "player 2": {"chess_id": self.player2.chess_id},
            "winner": {"chess_id": self.winner.chess_id} if self.winner else None
        }

    def set_winner(self, winner):
        """
        Set the winner of the match.

        Args:
        - winner (Player): The winner of the match.
        """
        self.winner = winner

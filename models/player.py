from _datetime import datetime


class Player:

    def __init__(self, first_name, last_name, date_of_birth, chess_id, points=0):
        """
        Initialize a Player instance.

        Args:
        - first name: The first name of the player.
        - last name: The last name of the player.
        - date of birth: The date of birth of the player.
        - chess_id: The identifier of the player.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = datetime.strptime(date_of_birth, '%Y-%m-%d')
        self.chess_id = chess_id
        self.points = points

    def to_dict(self):
        """
        Convert Player object to a dictionary.

        Returns:
        dict: Dictionary representation of the Player object.
        """
        return {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'date_of_birth': self.date_of_birth.strftime('%Y-%m-%d'),
            'chess_id': self.chess_id
         }

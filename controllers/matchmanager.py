import json
from models import Match
import random
from controllers.playermanager import PlayerManager


class MatchManager:

    def __init__(self):
        """
        Initialize MatchManager instance
        """
        self.json_file = "data/matches.json"
        self.matches = []
        self.load()
        self.player_manager = PlayerManager()

    def load(self):
        """
        Load matches from the JSON file and populate the matches list with Match instances.
        """
        self.matches = []
        with open(self.json_file, 'r') as f:
            data = json.load(f)
            for elem in data:
                player_manager = PlayerManager()
                player_manager.load()
                player1 = player_manager.find_by_id(elem['player 1']['chess_id'])
                player2 = player_manager.find_by_id(elem['player 2']['chess_id'])
                winner = player_manager.find_by_id(elem['winner']['chess_id']) if elem['winner'] else None

                match = Match(player1, player2, winner)
                match.id_match = elem['match_id']
                self.matches.append(match)

    def save(self):
        """
        Save the list of matches to a JSON file.
        """
        with open(self.json_file, 'w') as f:
            json.dump([match.to_dict() for match in self.matches], f, indent=2)

    def add_match(self, match):
        """
        Add a new match to the matches list and save the updated list to the JSON file.
        """
        self.load()
        self.matches.append(match)
        self.save()

    def add_match_data(self, player1, player2):
        m = Match(player1, player2)
        self.add_match(m)

    def simulate_match(self, match, tournament=None):
        """
        Simulate the result of a match by randomly selecting a winner or a draw.
        Args:
        - match (Match): The match to simulate.
        - tournament (Tournament): The tournament to which the match belongs, if applicable.
        """
        winner = random.choice([match.player1, match.player2, None])
        match.set_winner(winner)
        self.add_match(match)
        return winner

    def find_by_id(self, match_id):
        """
        Find a match in the matches list by its ID.
        Args:
        - match_id (int): The ID of the match to find.
        Returns:
        - Match: The match instance with the given ID, or None if not found.
        """
        for match in self.matches:
            if match.id_match == match_id:
                return match
        return None

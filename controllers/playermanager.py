import json
from models import Player
from views import PlayerView


class PlayerManager:

    def __init__(self):
        """
        Initialize PlayerManager instance.
        """
        self.json_file = "data/players.json"
        self.players = []
        self.view = PlayerView()

    def load(self):
        """
        Load the list of players from a JSON file.
        """
        self.players = []
        with open(self.json_file, 'r') as f:
            data = json.load(f)
            for elem in data:
                self.players.append(Player(**elem))

    def save(self):
        """
        Save the list of players to a JSON file.
        """
        with open(self.json_file, 'w') as f:
            json.dump([player.to_dict() for player in self.players], f, indent=2)

    def add_player(self, player):
        """
        Add a new player to the players list and save the updated list to the JSON file.
        Args:
        - player (Player): The Player instance to add.
        """
        self.load()
        if any(p.chess_id == player.chess_id for p in self.players):
            pass
        else:
            self.players.append(player)
            self.save()

    def add_player_data(self, f_name, l_name, d_birth, id):
        p = Player(f_name, l_name, d_birth, id)
        self.add_player(p)

    def add_player_in_tournament(self, player, tournament):
        """
        Add a player to a tournament.

        Args:
        - player (Player): The player to add to the tournament.
        - tournament (Tournament): The tournament to add the player to.
        """
        self.add_player(player)  # Add player to the player list.
        # Check if the player is already in the tournament before adding.
        if any(p.chess_id == player.chess_id for p in tournament.players):
            pass  # If player already exists in the tournament, do nothing.
        else:
            tournament.players.append(player)  # Add the player to the tournament.

    def find_by_name(self, player_name):
        """
        Find a player in the players list by their first name.
        """
        for player in self.players:
            if player.name == player_name:
                return player
        return None

    def find_by_id(self, player_id):
        """
        Find a player in the players list by their ID.
        """
        for player in self.players:
            if player.chess_id == player_id:
                return player
        return None

    def sorted_players_by_name(self):
        """
        Sort and return the players list by their first names.
        """
        self.load()
        players_by_name = sorted(self.players, key=lambda x: x.first_name)
        return players_by_name

    def get_player_name(self):
        """
        Prompt the user to input the first name of a player.
        """
        return input("Input the first name of the player : ")

    def manage_players_by_name(self):
        """
        Display a list of all players sorted by their first names
        """
        datas = self.sorted_players_by_name()
        self.view.show_players(datas)

import json
import random
from models import Tournament, Match, Round
from views import TournamentView
from controllers.matchmanager import MatchManager
from controllers.playermanager import PlayerManager


class TournamentManager:

    def __init__(self):
        """
        Initialize TournamentManager instance.
        """
        self.view = TournamentView()
        self.json_file = "data/tournaments.json"
        self.tournaments = []

    def create_tournament(self):
        """
        Create a new tournament and add it to the list of tournaments.

        Returns:
        Tournament: The created tournament.
        """
        name, place, start_date, end_date = self.view.prompt_create_tournament()
        tournament = Tournament(name, place, start_date, end_date)
        self.add_tournament(tournament)
        return tournament

    def find_by_name(self, tournament_name):
        """
        Find a tournament by its name
        """
        self.load()
        for tournament in self.tournaments:
            if tournament.name == tournament_name:
                return tournament
        return None

    def add_tournament(self, tournament):
        """
        Add a tournament to the list of tournaments
        """
        self.load()
        self.tournaments.append(tournament)
        self.save()

    def add_tournament_data(self, name, place, start_date, end_date):
        t = Tournament(name, place, start_date, end_date)
        self.add_tournament(t)

    def save(self):
        """
        Save the list of tournaments to a JSON file.
        """
        with open(self.json_file, 'w') as f:
            json.dump([tournament.to_dict() for tournament in self.tournaments], f, indent=4)

    def load(self):
        """
        Load the list of tournaments from a JSON file.
        """
        self.tournaments = []
        with (open(self.json_file, 'r') as f):
            data = json.load(f)
            for tournament_data in data:

                # reconstitute the tournament
                rounds = []
                tournament = Tournament(tournament_data['name'], tournament_data['place'],
                                        tournament_data['start_date'], tournament_data['end_date'],
                                        rounds)

                # reconstitute the rounds
                match_manager = MatchManager()
                match_manager.load()
                for round_data in tournament_data['rounds']:
                    round_obj = Round(round_data['round_number'])
                    for match_data in round_data['matches']:
                        match = match_manager.find_by_id(match_data['match_id'])
                        if match:
                            tournament.add_match(match, round_data['round_number'])
                        rounds.append(round_obj)

                # reconstitute the players
                player_manager = PlayerManager()
                player_manager.load()
                for p in tournament_data['players']:
                    player = player_manager.find_by_id(p['chess_id'])
                    player.points = p['points']
                    tournament.players.append(player)

                tournament.current_round = tournament_data.get('current_round', 0)

                self.tournaments.append(tournament)

    def sorted_players(self, tournament):
        """
        Sort the players list by point
        """
        tournament.players.sort(key=lambda s: s.points, reverse=True)

    def sorted_tournament_players_by_name(self, tournament):
        """
        Sort players list by the first name
        """
        self.load()
        players_by_name = sorted(tournament.players, key=lambda x: x.first_name)
        return players_by_name

    def generate_pairs(self, tournament, round_number):
        """
        Generate pairs of players for the given round in the tournament.
        Returns: list: List of player pairs.
        """
        if round_number == 1:
            self.mix_players(tournament)
        else:
            pass
        pairs = [(tournament.players[i], tournament.players[i + 1]) for i in range(0, len(tournament.players) - 1, 2)]

        return pairs

    def throw_round(self, tournament, round_number):
        """
        Execute a round in the specified tournament.
        :param tournament:
        :param round_number:
        """
        if round_number <= tournament.current_round:
            print(f"Round {round_number} already executed.")

        elif round_number == tournament.current_round + 1:
            pairs = self.generate_pairs(tournament, round_number)
            for p1, p2 in pairs:
                m = MatchManager()
                match = Match(p1, p2)
                winner = m.simulate_match(match, tournament)
                if winner is not None:
                    self.increment_points(tournament, winner.chess_id)
                tournament.add_match(match, round_number)
            self.sorted_players(tournament)
            tournament.current_round = round_number
            self.save()
        else:
            pass

    def mix_players(self, tournament):
        """
        Randomly shuffle the players in the tournament.
        """
        random.shuffle(tournament.players)

    def increment_points(self, tournament, player_chess_id):
        """
        Increment points for the specified player in the tournament.
        :param tournament:
        :param player_chess_id:
        """
        for player in tournament.players:
            if player.chess_id == player_chess_id:
                player.points += 1
                self.save()

    def manage_tournaments(self):
        """
        Display and manage all tournaments.
        """
        self.load()
        self.view.show_all_tournaments(self.tournaments)

    def get_tournament_name(self):
        return input("Give the tournament name : ")

    def manage_rounds(self, tournament):
        """
        Display and the rounds and the matches of a specific tournament.
        """
        self.load()
        self.view.display_rounds_and_matches(tournament.rounds)

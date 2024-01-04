from datetime import datetime
from models import Player


class TournamentView:

    def prompt_create_tournament(self):
        """
        Prompt the user to enter information for creating a tournament.
        Returns:
        tuple: Tuple containing tournament information (name, place, start_date, end_date).
        """
        print("Create a tournament")
        name = input("name of the tournament : ")
        place = input("place of the tournament : ")
        start_date = datetime.strptime(input("tournament start date in yyyy-mm-dd format : "),
                                       '%Y-%m-%d').strftime('%Y-%m-%d')
        end_date = datetime.strptime(input("tournament end date in yyyy-mm-dd format : "),
                                     '%Y-%m-%d').strftime('%Y-%m-%d')
        return name, place, start_date, end_date

    def prompt_add_player(self):
        """
        Prompt the user to enter player information for adding to a tournament.
        Returns:
        Player: A Player instance.
        """
        print("Add a player in the tournament")
        first_name = input("First name : ")
        last_name = input("Last name : ")
        date_of_birh = input("date of birth in format aaaa-mm-dd :"), '%Y-%m-%d'
        chess_id = input("identifier : ")
        return Player(first_name, last_name, date_of_birh[0], chess_id)

    def show_all_tournaments(self, tournaments):
        """
        Display information about all tournaments.
        Args:
        tournaments: List of Tournament instances to display.
        """
        print()
        print("The tournaments : ")
        for item in tournaments:
            print()
            print(item.name)

    def display_tournament_created(self):
        """
        Display a message indicating that a tournament has been successfully created.
        """
        print("The tournament has been created")

    def display_menu(self):
        print("Main Menu :")
        print("1 - Create a tournament")
        print("2 - Select a tournament")
        print("3 - Display alphabetically the players")
        print("4 - Quit")

    def display_tournament_submenu(self):
        print("Tournament Submenu :")
        print("1 - Display the list of tournaments")
        print("2 - Choose a tournament")
        print("3 - Back to main menu")

    def display_selected_tournament_submenu(self):
        print("Selected tournament submenu :")
        print("1 - Display the list of players alphabetically")
        print("2 - Display the list of rounds/matches")
        print("3 - Display the tournament infos")
        print("4 - Add a player")
        print("5 - Generate a round")
        print("6 - Back to the main submenu")

    def get_user_choice(self):
        return int(input("Enter a number: "))

    def display_invalid_choice(self):
        print("Choix invalide. Veuillez choisir à nouveau.")

    def display_rounds_and_matches(self, rounds):
        """
        Display information about the rounds and matches in a tournament.
        """
        for round in rounds:
            print(f"Round {round.round_number}:")
            for match in round.matches:
                print(
                    f"  Match ID: {match.id_match} : {match.player1.chess_id} vs {match.player2.chess_id}")

    def prompt_start_round(self):
        return int(input("Enter the round number to start: "))

    def show_tournament_info(self, tournament):
        """
        Display detailed information about a specific tournament.
        Args:
        tournament (Tournament): The tournament to display information about.
        """
        print()
        print("Info of the tournament : ")
        print("Name of the tournament :", tournament.name)
        print("Tournament Start date : ", tournament.start_date)
        print("Tournament End date : ", tournament.end_date)
        print()

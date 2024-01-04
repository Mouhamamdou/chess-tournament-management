class MenuManager:
    def __init__(self, tournament_manager, player_manager, match_manager, tournament_view, player_view):
        """
        Initialize MenuManager instance.
        """
        self.tournament_manager = tournament_manager
        self.player_manager = player_manager
        self.match_manager = match_manager
        self.tournament_view = tournament_view
        self.player_view = player_view

    def main_menu(self):
        """
        Display the main menu and handle user choices.
        Continuously runs until the user decides to exit.
        """
        while True:
            self.clear_screen()

            self.tournament_view.display_menu()

            choice = self.tournament_view.get_user_choice()

            if choice == 1:
                self.create_tournament()
            elif choice == 2:
                self.tournament_submenu()
            elif choice == 3:
                players = self.player_manager.sorted_players_by_name()
                self.player_view.show_players(players)
            elif choice == 4:
                break
            else:
                self.tournament_view.display_invalid_choice()

    def tournament_submenu(self):
        """
        Display the tournament submenu and handle user choices.
        Continuously runs until the user decides to return to the main menu.
        """
        while True:
            self.clear_screen()

            self.tournament_view.display_tournament_submenu()
            tournament_choice = self.tournament_view.get_user_choice()

            if tournament_choice == 1:
                self.tournament_manager.manage_tournaments()
            elif tournament_choice == 2:
                self.select_tournament()
            elif tournament_choice == 3:
                break
            else:
                self.tournament_view.display_invalid_choice()

    def select_tournament(self):
        """
        Handle the selection and management of a specific tournament.
        """
        name = self.tournament_manager.get_tournament_name()
        selected_tournament = self.tournament_manager.find_by_name(name)

        while True:
            self.tournament_view.display_selected_tournament_submenu()
            selected_tournament_choice = self.tournament_view.get_user_choice()

            if selected_tournament_choice == 1:
                players = self.tournament_manager.sorted_tournament_players_by_name(selected_tournament)
                self.player_view.show_players(players)
            elif selected_tournament_choice == 2:
                self.tournament_manager.manage_rounds(selected_tournament)
            elif selected_tournament_choice == 3:
                self.tournament_view.show_tournament_info(selected_tournament)
            elif selected_tournament_choice == 4:
                player = self.tournament_view.prompt_add_player()
                self.player_manager.add_player_in_tournament(player, selected_tournament)
                print([p.to_dict() for p in selected_tournament.players])
                self.tournament_manager.save()
            elif selected_tournament_choice == 5:
                self.execute_round(selected_tournament)
            elif selected_tournament_choice == 6:
                break
            else:
                self.tournament_view.display_invalid_choice()

    def create_tournament(self):
        self.tournament_manager.create_tournament()
        self.tournament_view.display_tournament_created()

    def clear_screen(self):
        # os.system('cls' if os.name == 'nt' else 'clear')
        print("\n" * 10)

    def execute_round(self, tournament):
        """
        Execute a round in a tournament.
        """
        round_number = tournament.current_round + 1
        self.tournament_manager.throw_round(tournament, round_number)

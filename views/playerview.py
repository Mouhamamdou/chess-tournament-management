class PlayerView:

    def show_players(self, datas):
        """
        Display information about all players.

        Args:
        datas (list): List of Player instances to display.
        """
        print()
        print("Players in alphabetical order. :")
        print()
        for item in datas:
            print("First name: ", item.first_name)
            print("Last name: ", item.last_name)
            print("Date of birth: ", item.date_of_birth)
            print("Identifier: ", item.chess_id)
            print()

    def display_player_added(self):
        """
        Display a message indicating that a player has been successfully added.
        """
        print("The player has been added")

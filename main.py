from controllers import TournamentManager, PlayerManager, MatchManager, MenuManager
from views import TournamentView, PlayerView


def main():
    tournament_manager = TournamentManager()
    player_manager = PlayerManager()
    match_manager = MatchManager()
    view_tournament = TournamentView()
    player_view = PlayerView()

    menu_manager = MenuManager(tournament_manager, player_manager, match_manager, view_tournament, player_view)

    while True:
        menu_manager.main_menu()


if __name__ == "__main__":

    main()

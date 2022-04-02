import unittest
from statistics import Statistics
from statistics import sort_by_points
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatistics(unittest.TestCase):
    def setUp(self):
        self.statistics = Statistics(
            PlayerReaderStub()
        )

        self.players = self.statistics._players

    def test_return_player_points(self):
        player = self.players[0]
        points = player.points

        points2 = sort_by_points(player)

        assert points == points2

    def test_search_player_by_name(self):
        player = self.players[0]
        player_name = player.name

        result = self.statistics.search(player_name)

        assert result == player

        result = self.statistics.search("keksitty_nimi")

        assert result == None

    def test_players_of_team(self):
        edm_players = ["Semenko", "Kurri", "Gretzky"]

        found_players = self.statistics.team("EDM")

        found_players_count = 0
        for player in found_players:
            if player.name in edm_players: found_players_count += 1

        assert found_players_count == 3

    def test_top_scorers_length(self):
        top_scorers = self.statistics.top_scorers(2)

        assert len(top_scorers) == 3


    




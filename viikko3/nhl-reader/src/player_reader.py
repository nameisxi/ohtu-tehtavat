from player import Player
import requests


class PlayerReader:
    def __init__(self, url):
        self.url = url

    def get_players(self, nationality):
        response = requests.get(self.url).json()
        players = []

        for player_dict in response:
            if player_dict['nationality'] != nationality: continue
            
            player = Player(
                player_dict['name'],
                player_dict['team'],
                player_dict['goals'],
                player_dict['assists'],
                player_dict['nationality']
            )

            players.append(player)

        return players

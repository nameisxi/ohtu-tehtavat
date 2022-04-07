import requests
import datetime
from player import Player

def main():
    url = "https://nhlstatisticsforohtu.herokuapp.com/players"
    response = requests.get(url).json()

    # print("JSON-muotoinen vastaus:")
    # print(response)

    players = []

    for player_dict in response:
        if player_dict['nationality'] != 'FIN': continue

        player = Player(
            player_dict['name'],
            player_dict['team'],
            player_dict['goals'],
            player_dict['assists']
        )

        players.append(player)

    print(f'Players from FIN {datetime.datetime.now()}')
    print()

    for player in players:
        print(player)

if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()

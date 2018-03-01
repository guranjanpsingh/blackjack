import BlackJack
from Player import Player
import helpers

if __name__ == '__main__':
    playerCount = 6
    players = []
    helpers.disabledPrint()
    for i in range(playerCount):
        player = Player(100, i + 1)
        players.append(player)
    simulationsToRun = 100
    for i in range(simulationsToRun):
        game = BlackJack.BlackJack(players, 6)
        game.play()

    helpers.enablePrint()
    for player in players:
        print("Player " + str(player.id) + " has " + str(player.balance) + ". Won " + str(
            player.winCount) + " rounds. Won " \
              + str(player.sideBetWinCount) + " side bets.")
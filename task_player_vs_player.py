'''
In this we try to create a player 1 vs player 2 situation. In this, every player is given the option to play the
tile of his choice from the tiles that can be played legally.
The decision and strategy is determined by the players.
The player has to enter his choice of tile in the prompt. If there is no legal tile to be played,
then the program automatically draws a tile for the user.
'''

import random

class DominoSet:
    def __init__(self):
        self.dominoSet = []                     # To store all the tiles
        self.player1 = []                       # To store tiles of player 1
        self.player2 = []                       # To store tiles of player 2
        self.playSet = []                       # To store which have been played in the game
        self.lastPlayerPlayed = ""              # To determine the last player to have played a tile. This is used to store the winner in case of a block

    # function createTile()
    def createTile(self):
        '''
        :param : None
        :return: None

        This function is used to create the set of Tiles. In this use case, we have 28 tiles
        with each tile ranging from (0:0) to (6:6).
        The maximum umber is '6' (called rank) in this use case.
        Each tile has 2 set of numbers (called pip). The pip varies from 0 till rank.
        Example -
        DominoSet - [(0, 0), (0, 1), (1, 1), (0, 2), (1, 2), (2, 2), (0, 3), (1, 3), (2, 3),
                    (3, 3), (0, 4), (1, 4), (2, 4), (3, 4), (4, 4), (0, 5), (1, 5), (2, 5),
                    (3, 5), (4, 5), (5, 5), (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6)]
        '''
        for rank in range(0, 7):
            for pip in range(0, rank + 1):
                self.dominoSet.append((pip, rank))
        # print(self.dominoSet)

    # function chooseRandomItem
    def chooseRandomItem(self):
        '''
        :param : None
        :return: randomTile

        This function chooses a random tile from the deck (dominoSet).
        Example - tile (4:5)
        '''
        randomTile = random.choice(self.dominoSet)
        self.dominoSet.remove(randomTile)
        return randomTile

    # function drawTilesForPlayers
    def drawTilesForPlayers(self):
        '''
        :param : None
        :return: None

        This function is used to draw tiles, initially, from domino stack for both players
        (7 for this use case). The tiles are chosen randomly from the domino stack.
        Example -
        Player 1:  [(1, 2), (0, 0), (0, 3), (5, 6), (2, 3), (4, 4), (3, 6)]
        Player 2:  [(2, 5), (3, 5), (2, 6), (1, 1), (3, 4), (1, 4), (4, 6)]
        '''
        self.player1 = [self.chooseRandomItem() for _ in range(7)]
        self.player2 = [self.chooseRandomItem() for _ in range(7)]
        # print("Player 1: ", self.player1)
        # print("Player 2: ", self.player2)

    # function checkPositions
    def checkPositions(self, nextTile, previousTile, player):
        '''

        :param nextTile: The next tile which will be played by the player
        :param previousTile: The previous tile which was played by the player
        :param player: Current player
        :return:
            nextTile: The next tile which will be played by the player

        Logic:
        This function is used to determine if the next tile is played in the same order or the reverse order.
        This is based on the position of the previous tile.
        In the sense that if the previous tile was (0:2), and the next tile was (4:2), then the tile will be played in the
        reverse order - (2:4) to match the order of the previous tile.
        Example - 1. if previousTile == (1:3) and nextTile == (5:3)
                        then nextTile == (3:5) (order if reversed)
                  2. if previousTile == (1:1) and  nextTile == (1:4)
                        then nextTile is (1:4) (order is not reversed)
        '''
        if previousTile[1] == nextTile[0]:
            print()
            print("Player {0} plays the tile {1}".format(player, nextTile))
        else:
            nextTile = (nextTile[1], nextTile[0])
            print()
            print("Player {0} plays the tile {1}".format(player, nextTile))
        return nextTile

    # function checkTileValidity
    def checkTileValidity(self, playableTiles):
        '''

        :param playableTiles: All the tiles that can be played. The user has to select one from these!
        :return: tileNumber: The tile number which is selected by the user to be played

        Logic: If there are tiles that can be played, ask the user to enter tile number until a valid tile
                number is entered. (hence the infinite loop).
        '''
        while True:
            tileNumber = input("Please select a tile to play. Enter the tile number to play \n "
                               "(type 1 for the 1st tile and so on) : \n \n")
            if not tileNumber.isnumeric():
                print()
                print("Please enter a valid tile number")
                print()
                continue
            elif int(tileNumber) > len(playableTiles):              # TODO : may be this if statement can be combined with first if statement
                print()
                print("Please enter a valid tile number")
                print()
                continue
            else:
                break
        return int(tileNumber)

    # playGame
    def playGame(self):
        '''
         Parameters : None
        :return:

        Logic:
        This function is the initial point to begin the game. It uses an infinite loop concept and the loop breaks when
        either - 1. Player 1 has no tiles to play
            or - 2. Player 2 has no tiles to play
            or - 3. There are no more tiles to be drawn from the stack.
            In the last case, the last player to play a tile wins the game.
        '''
        print()
        print()
        print("Game Begins")
        print()

        # Choose a player randomly among the 2 players
        currentPlayer = random.choice(["1", "2"])

        print("Player {0} begin the game!".format(currentPlayer))
        print()

        if currentPlayer == "1":
            playerDeck = self.player1
            nextPlayer = "2"
        else:
            playerDeck = self.player2
            nextPlayer = "1"

        print("The tiles available to Player {0} are: ".format(currentPlayer))      # Print the tiles of current player
        print(playerDeck)
        print()
        tileNumber = self.checkTileValidity(playerDeck)                             # Ask the user to select a tile
        firstTile = playerDeck[tileNumber - 1]
        playerDeck.remove(firstTile)
        self.playSet.append(firstTile)
        print()
        print("Player {0} plays a tile: {1}".format(currentPlayer, firstTile))      # Print the tile played by the user
        print()
        currentPlayer = nextPlayer                                              # The next chance is for the next player
        previousTile = firstTile
        while True:
            # Check if player 1 or player 2 has any tiles left to play or if any more tiles are left on the domino stack
            if len(self.player1) > 0 and len(self.player2) > 0 and len(self.dominoSet) > 0:
                previousTile, currentPlayer = self.gamePlay(previousTile, currentPlayer)
            elif len(self.player1) == 0:        # Player 1 has no more tiles in his deck. Hence he wins
                print("Player 1 wins!")
                break
            elif len(self.player2) == 0:         # Player 2 has no more tiles in his deck. Hence he wins
                print("Player 2 wins!")
                break
            elif len(self.dominoSet) == 0:       # There are no more tiles left to be drawn from domino stack. Hence the last player to play a tile wins.
                print()
                print("Player {0} wins the game (as last played) with no more tiles to draw from deck!".format(self.lastPlayerPlayed))
                print()
                print("Tile Set sequence is: ", self.playSet)
                exit()
        return

    # function gamePlay
    def gamePlay(self, previousTile, currentPlayer):
        '''

        :param previousTile: The previous tile which was played by the player
        :param currentPlayer: The current player to play or draw a tile
        :return: nextTile : The tile played (if possible) by the player, or the previous tile (if tile is drawn
                            from the stack and cannot play a tile)
                 nextPlayer: Next players turn

        Logic:
        Based on the current player, his deck is checked for tiles that can be played. If suitable matches are
        found, then ask the user to enter the tile to be played. Play this tile after checking the order.
        If no matches are found then, if there are tiles that can drawn from the domino stack, then a random tile
        is drawn from the domino stack. If this tile can be played, then the user is asked to play it,
        else the next chance goes to the next player.
        If a player plays a tile and there are no more tiles in his deck, then that player wins.
        '''

        if currentPlayer == "1":
            playerDeck = self.player1
            nextPlayer = "2"                # Next players turn
        elif currentPlayer == "2":
            playerDeck = self.player2
            nextPlayer = "1"                # Next players turn

        print()
        print("Player {0} to play!".format(currentPlayer))
        print()
        print("The tiles available to Player {0} are: ".format(currentPlayer))      # Print tiles available to current player
        print(playerDeck)
        print()
        playableTiles = [item for item in playerDeck                        # Tiles that can be played legally
                         if item[0] == previousTile[1] or item[1] == previousTile[1]]
        # print("playableTiles: ", playableTiles)

        if len(playableTiles) > 0:                              # If playable tiles exist, then play
            print("Tiles that can be played by player {0} are: ".format(currentPlayer)) # Print those tiles that can be played
            print(playableTiles)
            print()

            tileNumber = self.checkTileValidity(playableTiles)                     # Ask the user to select a tile
            nextTile = playableTiles[tileNumber - 1]
            playerDeck.remove(nextTile)
            nextTile = self.checkPositions(nextTile, previousTile, currentPlayer)
            self.playSet.append(nextTile)
            print()
            print("The current played deck is: ")
            print()
            print(self.playSet)
            self.lastPlayerPlayed = currentPlayer
            if len(playerDeck) == 0:
                print()
                print("Player {0} wins the game with no more tiles to play from him!".format(self.lastPlayerPlayed))
                print()
                print("Tile Set sequence is: ", self.playSet)
                exit()
        else:                                               # Else, draw from the domino stack
            if len(self.dominoSet) > 0:                     # Check if there are tiles available on domino stack
                tileToAddToPlayer = random.choice(self.dominoSet)
                print("Player {0} draws from the domino stack".format(currentPlayer))
                self.dominoSet.remove(tileToAddToPlayer)

                # Check if the drawn tile can be played immediately, else add the tile to the current player's deck
                if tileToAddToPlayer[0] == previousTile[1] or tileToAddToPlayer[1] == previousTile[1]:
                    print()
                    print("Tiles that can be played by player {0} are: ".format(currentPlayer))
                    print(tileToAddToPlayer)
                    print()
                    tileNumber = self.checkTileValidity(tileToAddToPlayer)      # Ask the user to select the drawn tile
                    nextTile = self.checkPositions(tileToAddToPlayer, previousTile, currentPlayer)
                    self.playSet.append(nextTile)
                    self.lastPlayerPlayed = currentPlayer
                else:
                    playerDeck.append(tileToAddToPlayer)
                    nextTile = previousTile

        return nextTile, nextPlayer


dominoSet = DominoSet()
dominoSet.createTile()
dominoSet.drawTilesForPlayers()
dominoSet.playGame()

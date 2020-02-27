from hungrytigeragent import HungryTigerAgent
from agent import Agent
from const import Const
from game import Game
from move import Move
from typing import List
import random

class DontYouDareTiger(Agent):
    def __init__(self, game : Game):
        super(DontYouDareTiger, self).__init__(game,Const.MARK_GOAT)
        self._hungryTigerAgent = HungryTigerAgent(game)

    def propose(self) -> Move:
        moves = self.game.goatMoves()
        tigerMovement = self.game.tigerMoves() 

        safe : List[Move]=[]
        willBeEaten: List[Move] = []
        preferedChoice: List[Move] = []
        for move in moves:
            if move.toRow == 0 and move.toCol == 0:
                safe.append(move)
            if move.toRow == 4 and move.toCol == 0:
                safe.append(move)
            if move.toRow == 4 and move.toCol == 4:
                safe.append(move)
            if move.toRow == 0 and move.toCol == 4:
                safe.append(move)
            
            for movements in tigerMovement:
                if abs(movements.toRow - move.toRow) == 1:
                    willBeEaten.append(move)
                else:
                    safe.append(move)

                if abs(movements.toCol - move.toCol) == 1:
                    willBeEaten.append(move)
                else:
                    safe.append(move)
            preferedChoice.append(random.choice(safe))
        if preferedChoice != 0:
            return random.choice(preferedChoice)
        else:
            return random.choice(moves)
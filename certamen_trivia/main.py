import player
import quote
import theme
import visual
import image
import board

import pygame




if __name__ == "__main__":
    board = board.Board()
    board.retrieve_questions()
    board.run()



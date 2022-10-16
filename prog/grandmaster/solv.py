#!/usr/bin/env python3
from pwn import *
import chess
import chess.engine
from stockfish import Stockfish

piecedict = {"Piece.WHITE_KNIGHT":"N", "Piece.WHITE_QUEEN":"Q", "Piece.WHITE_BISHOP":"B","Piece.WHITE_KING":"K", "Piece.WHITE_PAWN":"","Piece.WHITE_ROOK":"R"}

def genFEN(board):
    FEN = ""
    for line in board.split("\n"):
        a = 0
        for tegn in line:
            if tegn == ".":
                a+=1
            elif tegn == " ":
                continue
            else:
                if a != 0:
                    FEN += str(a)
                FEN += tegn
                a = 0
        if a != 0:
            FEN += str(a)
        FEN += "/"
    FEN = FEN[:-2] + " w - - 1 1"
    return FEN
                

engine = chess.engine.SimpleEngine.popen_uci("/usr/games/stockfish")

stockfish = Stockfish("/usr/games/stockfish")


r = remote("grandmaster.deadface.io",5000)
moves = r.recv().decode()
brett = r.recv(4096).decode()
print(brett)
brett = genFEN(brett)
print(brett)
brettet = chess.Board(brett)

stockfish.set_fen_position(brett)
bestmove = stockfish.get_best_move()

piece = stockfish.get_what_is_on_square(bestmove[:2]).value
if stockfish.will_move_be_a_capture(bestmove).value != "no capture":
    capture = "x"
else:
    capture = ""
bestmove = piece + capture + bestmove[2:]
print(bestmove)


r.sendline(bestmove)
print(r.recv().decode())

engine.quit()
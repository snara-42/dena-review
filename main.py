import re
import sys
import argparse

def main():
    parser = argparse.ArgumentParser(description="a connect-four game.")
    parser.add_argument("-p1", "-player1", type=str, default="x", help="disc for player 1")
    parser.add_argument("-p2", "-player2", type=str, default="o", help="disc for player 2")
    parser.add_argument("-e", "-empty", type=str, default=".", help="empty slot")
    parser.add_argument("-y", "-height", type=int, default=6, help="board height")
    parser.add_argument("-x", "-width", type=int, default=7, help="board width")
    # parser.add_argument("-l", "-length", type=int, default=4, help="length to win")
    args = parser.parse_args()
    print(args)

if __name__ == '__main__':
    main()

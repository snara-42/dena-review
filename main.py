import argparse
import game


def main():
    parser = argparse.ArgumentParser(description="a connect-four game.")
    parser.add_argument("-p1", "-player1", type=str, default="x",
                        help="symbol for player 1 (default 'x')")
    parser.add_argument("-p2", "-player2", type=str, default="o",
                        help="symbol for player 2 (default 'o')")
    parser.add_argument("-e", "-empty", type=str, default=".",
                        help="symbol for empty slot (default '.')")
    parser.add_argument("-s", "-separator", type=str, default=" ",
                        help="for separating numbers (default ' ')")
    parser.add_argument("-x", "-width", type=int, default=7,
                        help="board width (default 7)")
    parser.add_argument("-y", "-height", type=int, default=6,
                        help="board height (default 6)")
    parser.add_argument("-n", "-length", type=int, default=4,
                        help="length to win (default 4)")
    parser.add_argument("-o", "-logfile", type=str, default="result.log",
                        metavar="FILE", help="file to save log (default 'result.log')")
    args = parser.parse_args()

    g = game.Game(**vars(args))
    g.play()


if __name__ == '__main__':
    main()

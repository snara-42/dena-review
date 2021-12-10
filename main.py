import re
import argparse


class Game:
    def __init__(self, **kw):
        self.x = kw.get("x", 7)
        self.y = kw.get("y", 6)
        self.len = kw.get("len", 4)
        self.sym = [kw.get("e", "."), kw.get("p1", "x"), kw.get("p2", "o"), ]
        self.logfile = kw.get("o", "result.log")
        self.board = ["" for _ in range(self.x)]

    def __str__(self):
        return "\n".join((*[" ".join(s).translate(str.maketrans({k: v for k, v in zip(".xo", self.sym)})) for s in zip(*[col.ljust(self.y, ".")[::-1] for col in self.board])], self.sym[0].join([str(i) for i in range(1, self.x+1)])))+"\n"

    @staticmethod
    def input_int(prompt):
        while True:
            try:
                return int(input(prompt).strip())
            except ValueError:
                continue

    def input_valid_index(self, prompt):
        while True:
            n = self.input_int(prompt)
            if 1 <= n <= self.x and len(self.board[n-1]) < self.y:
                return n

    def has_won(self, c: str):
        reg = re.compile(
            "(("+c+"){"+str(self.len)+"})"
            + "|(("+c+".{"+str(self.y-1)+"}){"+str(self.len-1)+"}"+c+")"
            + "|(("+c+".{"+str(self.y) + "}){"+str(self.len-1)+"}"+c+")"
            + "|(("+c+".{"+str(self.y+1)+"}){"+str(self.len-1)+"}"+c+")")
        return reg.search("/".join(c.ljust(self.y, ".") for c in self.board))

    def play_round(self):
        for i in range(self.x * self.y):
            print(f"\n{self}{i+1} player{i%2+1}[{self.sym[i%2+1]}]'s turn")
            n = self.input_valid_index("> ")
            c = "xo"[i % 2]
            self.board[n-1] += c
            if self.has_won(c):
                res = f"\n{self}player{i%2+1}[{self.sym[i%2+1]}] wins!\n"
                print(res)
                break
        else:
            res = f"\n{self}draw!\n"
            print(res)
        try:
            with open(self.logfile, "a") as f:
                f.write(res)
        except Exception as e:
            print(e)
        input("\nPress enter to play again... ")

    def play(self):
        try:
            while True:
                self.board = ["" for _ in range(self.x)]
                self.play_round()
        except EOFError:
            return


def main():
    parser = argparse.ArgumentParser(description="a connect-four game.")
    parser.add_argument("-p1", "-player1", type=str, default="x",
                        help="symbol for player 1")
    parser.add_argument("-p2", "-player2", type=str, default="o",
                        help="symbol for player 2")
    parser.add_argument("-e", "-empty", type=str, default=".",
                        help="symbol for empty slot")
    parser.add_argument("-x", "-width", type=int, default=7,
                        help="board width")
    parser.add_argument("-y", "-height", type=int, default=6,
                        help="board height")
    parser.add_argument("-len", "-length", type=int, default=4,
                        help="length to win")
    parser.add_argument("-o", "-logfile", type=str, default="./result.log",
                        metavar="FILE", help="file to save results")
    args = parser.parse_args()

    print(args)
    game = Game(**vars(args))
    game.play()


if __name__ == '__main__':
    main()

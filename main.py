import re
import argparse




class Game:
    def __init__(self, d: dict):
        self.x = d.get("x", 7)
        self.y = d.get("y", 6)
        self.len = d.get("len", 4)
        self.sym = [d.get("e", "."), d.get("p1", "x"), d.get("p2", "o"), ]
        self.board = ["" for _ in range(self.x)]

    def __str__(self):
        return "\n".join((*[" ".join(s).translate(str.maketrans({k: v for k, v in zip(".xo", self.sym)})) for s in zip(*[col.ljust(self.y, ".")[::-1] for col in self.board])], self.sym[0].join([str(i) for i in range(1, self.x+1)])))

    @staticmethod
    def input_int(prompt):
        while True:
            try:
                n = int(input(prompt).strip())
                return n
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
        print(reg)
        return reg.search("/".join(c.ljust(self.y, ".") for c in self.board))

    def play_round(self):
        for i in range(self.x * self.y):
            print(self, f"\n{i+1} player{i%2+1}[{self.sym[i%2+1]}]'s turn")
            n = self.input_valid_index("> ")
            c = "xo"[i % 2]
            self.board[n-1] += c
            if self.has_won(c):
                print(self, f"\nplayer{i%2+1}[{self.sym[i%2+1]}] wins!\n\n")
                break
        else:
            print(self, "\ndraw!\n\n")
        input("\nPress enter to play again ")

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
    args = parser.parse_args()

    game = Game(vars(args))
    game.play()


if __name__ == '__main__':
    main()

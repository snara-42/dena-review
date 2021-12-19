import re


class Game:
    def __init__(self, **kw):
        self.x = kw.get("x", 7)
        self.y = kw.get("y", 6)
        self.n = kw.get("n", 4)
        if not (1 <= self.n <= min(self.x, self.y)):
            raise ValueError("values must satisfy 1 <= n <= min(x, y)")
        self.sym = [kw.get("e", "."), kw.get("p1", "x"), kw.get("p2", "o"),
                    kw.get("s", " ")]
        self.logfile = kw.get("o", "result.log")
        self.board = ["" for _ in range(self.x)]

    def __str__(self):
        tr = str.maketrans(dict(zip(".xo_", self.sym)))
        s = "\n"
        for row in zip(*[f"{col:.<{self.y}}"[::-1] for col in self.board]):
            s += "|"+" ".join(row)+"|\n"
        s += "-_"*self.x + "-\n "\
            + "_".join(f"{i+1}" for i in range(self.x))+"\n"
        return s.translate(tr)

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
            "(("+c+"){"+str(self.n)+"})"
            + "|(("+c+".{"+str(self.y-1)+"}){"+str(self.n-1)+"}"+c+")"
            + "|(("+c+".{"+str(self.y) + "}){"+str(self.n-1)+"}"+c+")"
            + "|(("+c+".{"+str(self.y+1)+"}){"+str(self.n-1)+"}"+c+")")
        return reg.search("/".join(f"{col:.<{self.y}}" for col in self.board))

    def write_log(self, res):
        print(res)
        try:
            with open(self.logfile, "a") as f:
                f.write(res)
        except Exception as e:
            print(e)

    def play_round(self):
        self.board = ["" for _ in range(self.x)]
        for i in range(self.x * self.y):
            print(f"{self}{i+1}: player{i%2+1}[{self.sym[i%2+1]}]'s turn")
            n = self.input_valid_index("> ")
            c = "xo"[i % 2]
            self.board[n-1] += c
            if self.has_won(c):
                self.write_log(
                    f"{self}player{i%2+1}[{self.sym[i%2+1]}] wins!\n")
                break
        else:
            self.write_log(f"{self}draw!\n")
        if input("Press enter to play again (q to exit)\n").strip().casefold() in ("q", "exit"):
            raise EOFError

    def play(self):
        try:
            while True:
                self.play_round()
        except EOFError:
            print("bye!")
            return

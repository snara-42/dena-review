## dena-review


### usage
```python main.py```
```
optional arguments:
  -h, --help             show help message and exit

  -p1 P1, -player1 P1    symbol for player 1   (default 'x')
  -p2 P2, -player2 P2    symbol for player 2   (default 'o')
  -e E, -empty E         symbol for empty slot (default '.')
                         (for better experience, P1, P2 and E should have the same width)
  -x X, -width X         board width   (default 7)
  -y Y, -height Y        board height  (default 6)
  -n N, -length N        length to win (default 4)
                         (N must be 1 <= N <= min(x, y))
  -o FILE, -logfile FILE file to save results
```

### examples


![game screenshot](docs/screenshot1.png)

```python main.py -p1 "🟥" -p2 "🟢" -e "・" -x 8 -y 7```

![game screenshot](docs/screenshot2.png)


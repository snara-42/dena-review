## dena-review


### usage
```
python main.py
```

Players take turns dropping a disc on one of the columns.  
The objective is to make a straight line of `N` discs of yours (horizontally, vertically, or diagonally).  
The game is over when one of the players makes a line, or there is no more empty slot on the board.

Here's what you can modify with arguments:  
 - discs & empty slots (can be a multi-byte or multi-character string)
 - separator (better be a few space characters with the same width as above)
 - width and height of the game board
 - number of discs needed to win
 - file to append result when the game is over

```
optional arguments:
  -h, --help             show help message and exit

  -p1 P1, -player1 P1    symbol for player1's disc   (default 'x')
  -p2 P2, -player2 P2    symbol for player2's disc   (default 'o')
  -e E, -empty E         symbol for empty slots      (default '.')
  -s S, -separator S     string between column numbers (default ' ')
  (for better looking, P1, P2, E, and S should have the same width)

  -x X, -width X         board width   (default 7)
  -y Y, -height Y        board height  (default 6)
  -n N, -length N        length to win (default 4)
  (must satisfy 1 <= N <= min(x, y))

  -o FILE, -logfile FILE file to save results (default "./result.log")
                         pass an empty string "" if not needed

```

### examples

```
python main.py
```
<img width="159" alt="screenshot1" src="https://user-images.githubusercontent.com/77873284/146698060-b270a027-28fd-457a-93e9-7c380a7d9132.png">

```
python main.py -p1 "🟥" -p2 "🟢" -e "・" -s "　" -x 5 -y 5
```
<img width="267" alt="screenshot2" src="https://user-images.githubusercontent.com/77873284/146698096-79f952ba-3e92-49e3-b8e4-0c258cb3cac7.png">

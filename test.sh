rm -f test.log

python main.py -h

python main.py -p1 "🟥" -p2 "🟢" -e "🔼" -s "　" -o test.log << _
1
1
1
1
1
1
2
2
2
2
2
2
3
3
3
3
3
3
5
5
5
5
5
5
6
6
6
6
6
6
7
7
7
7
7
4
4
4
4
4
4
7
_
#draw

python main.py -p1 "#" -p2 "$" -e "_" -o test.log << _
1
1
2
2
3
3
4
_
#x-

python main.py -p1 "!" -p2 "|" -e ":" -o test.log << _
1
2
1
2
1
2
1
_
#x|

python main.py -p1 "/" -p2 "\\" -e "-" -o test.log << _
1
2
2
1
3
3
3
4
4
4
4
_
#x/

python main.py -p1 "/" -p2 "\\" -e "^" -o test.log << _
5
4
5
4
5
4
4
6
7
7
6
_
#x\ 

python main.py -p1 "ῷ" -p2 "ἔ" -e "•" -o test.log << _
3
2
3
2
3
2
1
1
1
2
_
#o|

python main.py -p1 "歩" -p2 "と" -e "王" -s "  " -x 9 -y 9 -o test.log << _
7
7
7
7
7
7
6
6
6
6
6
6
5
5
5
5
5
5
3
4
4
4
4
4
3
4
_
#o-

python main.py -p1 "eax" -p2 "mov" -e "___" -s "   " -x 5 -o test.log << _
1
1
1
1
1
1
3
2
2
2
2
2
2
3
3
3
3
3
4
4
4
4
5
4
_
#o/

python main.py -n 5 -o test.log << _
1
1
1
1
1
1
3
2
2
2
2
2
2
3
3
3
3
3
6
4
4
4
4
4
4
5
6
5
_
#o\ 

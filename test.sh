rm -f test.log
python main.py -o test.log << EOF
#draw#
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

#x-#
1
1
2
2
3
3
4

#x|#
1
2
1
2
1
2
1

#x/#
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

#x\ #
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

#o|#
1
1
2
1
2
1
2
1

#o-#
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

#o/#
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
3
4
4
4
4
5
4

#o\ #
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
3
5
4

EOF

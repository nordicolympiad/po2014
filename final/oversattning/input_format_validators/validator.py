#/usr/bin/env python
import re
import sys

input_re1 = "^[1-9][0-9]*$"
input_re2 = "^[a-z]+ [a-z]+$"
input_re3 = "^[a-z]+$"

line = sys.stdin.readline()
assert re.match(input_re1, line)

N = int(line)

assert 1 <= N <= 50000

words = {}

for i in xrange(N):
    line = sys.stdin.readline()
    assert re.match(input_re2, line)
    w1, w2 = line.split()
    words[w1] = w2
    assert 1 <= len(w1) <= 20
    assert 1 <= len(w2) <= 20

line = sys.stdin.readline()
assert re.match(input_re1, line)
M = int(line)

assert 1 <= M <= 100000

line = sys.stdin.readline()
wordlist = line.split()

assert len(wordlist) == M

for i in xrange(len(wordlist)):
    w = wordlist[i]
    assert re.match(input_re3, w)
    assert 1 <= len(w) <= 20
    assert w in words

line = sys.stdin.readline()
assert len(line) == 0
sys.exit(42)

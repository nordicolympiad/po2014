#/usr/bin/env python
import re
import sys
input_re = "^\d{4,12}$"
line = sys.stdin.readline()
assert re.match(input_re, line)
line = sys.stdin.readline()
assert len(line) == 0
sys.exit(42)

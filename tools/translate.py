
import sys
from pattern import *

if len(sys.argv) == 0:
	sys.exit("usage: translate.py eip")
else:
	eip = sys.argv[1]
	eip = [eip[i:i+2] for i in range(0, len(eip), 2)]
	eip = eip[::-1]
	eip = map(lambda x: chr(int(x, 16)), eip)
	eip = "".join(eip)
	pattern = "".join(pattern_create(8000))
	print "substring: " + eip
	print "position: " + str(pattern.find(eip))

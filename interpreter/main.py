from tokenizer, parser import *
import sys
with open(sys.argv[1], 'r') as script:
	for line in script.read():
		parse(tokenize(line))
import sys

if len(sys.argv) > 1:
	thing = sys.argv[1]
else:
	thing = "4-'3evh?'c)7%t#e-r,g6u#.9uv#%tg2v#7g'w6gA"

for i in thing:
	val = ord(i) + 60
	if val > 122:
		val -= 94
	print(chr(val), end='')

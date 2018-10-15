import sys

sys.argv = sys.argv[1:]

counter = 0
things = []

print("0x", end='');

for i in sys.argv:
	things.append(hex(int(i, 2))[2:])
	counter += 1
	if counter == 4:
		for a in reversed(things):
			print(a, end='')
		counter = 0
		print(' 0x', end='')
		things = []
for a in reversed(things):
	print(a, end='')
for i in range(counter, 4):
	print("00", end='');
print()

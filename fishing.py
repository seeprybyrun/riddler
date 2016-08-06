import random

k = 10
N = 1000000

total_eaten_with_constraint = {}

for p in range(0,k+1):
	cutoff = (p*1.0)/k
	total = 0

	for i in range(N):
		x1 = random.random()
		if x1 >= cutoff:
			total += x1

		x2 = random.random()
		if x2 >= x1 or x1 < cutoff:
			total += x2

	print "Average eaten if first fish skipped when weight < {}: {}".format(cutoff, total/N)

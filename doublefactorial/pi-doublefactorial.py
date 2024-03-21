from sys import argv
import math

pi = 0

print("Performing " + argv[1] + " loops")
for k in range(int(argv[1])):
	pi += (2 ** k * math.factorial(k) ** 2) / (math.factorial(2 * k + 1))

	if len(argv) >= 3:
		print("\033[0;37m" + str(k) + ":\033[0;32m π = " + str(pi * 2).ljust(20, " ") + " \033[0;37m| \033[0;36mk = " + str(k))

pi *= 2
print("\033[1;32mπ = " + str(pi))

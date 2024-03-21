from sys import argv
import matplotlib.pyplot as plt
import numpy as np

k = 1
pi = 0

x = np.arange(0, int(argv[1]), 1)
y = np.array([])
 
print("Performing " + argv[1] + " loops")

for i in range(int(argv[1])):
    if i % 2 == 0:
        pi += 4 / k
    else: 
        pi -= 4 / k
    k += 2

    if len(argv) >= 3:
        print("\033[0;37m" + str(i) + ":\033[0;32m π = " + str(pi).ljust(20, " ") + " \033[0;37m| \033[0;36mk = " + str(k))
    y = np.append(y, pi)

print("\033[1;32mπ = " + str(pi))

plt.title ("Calculating π")
plt.xlabel("Iterations of Leibniz's formula")
plt.ylabel("Estimation")
plt.plot  (x, y)
plt.show  ()
from sys import argv

k = 1
pi = 0
 
for i in range(int(argv[1])):
    if i % 2 == 0:
        pi += 4 / k
    else: 
        pi -= 4 / k
    k += 2

    if len(argv) >= 3:
        print("\033[0;37m" + str(i) + ":\033[0;32m π = "+str(pi).ljust(20, " ") + " \033[0;37m| \033[0;36mk = " + str(k))

print("\033[1;32mπ = " + str(pi))
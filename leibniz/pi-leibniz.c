#include <stdio.h>
#include <stdlib.h>

double k = 1;
double pi = 0;

int main(int argc, char *argv[]) {
	printf("Performing %s loops\n", argv[1]);

	for(int i = 0; i < atoi(argv[1]); i++) {
		if(i % 2 == 0) pi += 4 / k;
		else pi -= 4 / k;
		k += 2;
		if(argc >= 3) printf("\033[0;37m%d: \033[0;32mπ = %f \033[0;37m| \033[0;36mk = %f\n", i, pi, k);
	}

	printf("\033[1;32mπ = %f\n", pi);
}

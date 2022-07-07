#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "coeffs.h"

int main(){

void triangular(char *str, int len){
double sum;
FILE *fp;
fp = fopen(str,"w");
for (int i = 0; i < len; i++){
	sum = 0;
	for (int j = 0; j < 2; j++){
	sum += (double)rand()/RAND_MAX;
	}
	fprintf(fp,"%lf\n",sum);
       }
fclose(fp);
}

triangular("tri.dat", 1000000);

return 0;
}

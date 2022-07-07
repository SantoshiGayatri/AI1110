#include <stdio.h>
#include <stdlib.h>
#include <math.h>

void v(char *str, int len){
int i;
FILE *fp;

fp = fopen(str,"w");
for (i = 0; i < len; i++){
fprintf(fp,"%lf\n",-2*log(1-(double)rand()/RAND_MAX));
}
fclose(fp);
}

int main(){
v("v.dat", 1000000);
return 0;
}

#include <stdio.h>
#include <stdlib.h>

int main(){
    FILE *fp;
    fp=fopen("uni.dat","r");
    double sum,x,y=0;
    int i=0;
    while(fscanf(fp,"%lf",&x)!=-1){
        sum+=x;i++;
    }
    fclose(fp);

    y=sum/1000000;
    printf("mean = %lf\n",y);

    fp=fopen("uni.dat","r");
    double sqr,z=0;
    int j=0;
    while(fscanf(fp,"%lf",&z)!=-1){
        sqr+=(z-y)*(z-y);
        j++;
    }
    fclose(fp);

    double var=sqr/1000000;
    printf("variance = %lf\n",var);
    return 0;
}

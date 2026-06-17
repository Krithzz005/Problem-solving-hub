#include<stdio.h>

int main(void) {
    int binArr[32];
    int i=0,j;
    
    int dec;
    
    dec  = 32;
    
    while(dec>0){
        binArr[i]=dec%2;
        dec /= 2;
        i++;
    }
    int count=0;
    for(j=i-1;j>=0;j--){
        if (binArr[j]==1){
            count+=1 ; 
        }
        printf("%d",binArr[j]);
    }
    printf("\n");
    if (count==0){
        printf("Invalid");
    }else{
        printf("%d\n",count);
    }
return 0;
}

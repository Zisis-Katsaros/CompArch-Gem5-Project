#include <stdio.h>

int sum_of_ints_up_to_N(int N){
    int sum = 0;
    for (int n = 1; n<N+1; n++){
        sum = sum + n;
    }
    return sum;
} 


int main()
{
    int sum = sum_of_ints_up_to_N(8);
    printf("%d", sum);
    return 0;
}
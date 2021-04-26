#include <stdio.h>
int main()
{
    int var = 10;
    int sum = 0;

    for (int i = 0; i < 5; i++)
    {
        sum += 10 * i;
    }

    printf("Sum: %d", sum);

    return 0;
}

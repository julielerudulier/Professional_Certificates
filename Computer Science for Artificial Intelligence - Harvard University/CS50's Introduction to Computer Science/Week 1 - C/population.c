#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Prompts for start size:
    int start;
    do
    {
        start = get_int("Start size? ");
    }
    while (start < 9);

    // Prompts for end size:
    int end;
    do
    {
        end = get_int("Goal size? ");
    }
    while (end < start);

    // Calculates number of years until we reach threshold:
    int n = 0;
    while (start < end)
    {
        start = start + start / 3 - start / 4;
        n++;
    }

    // Prints number of years:
    printf("Years: %i\n", n);
}

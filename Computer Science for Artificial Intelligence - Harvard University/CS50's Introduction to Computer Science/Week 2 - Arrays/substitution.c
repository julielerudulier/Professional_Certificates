#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

int main(int argc, string argv[])
{
    if (argc != 2)
    {
        printf("Usage: ./substitution invalid key\n");
        return 1;
    }

    int len = strlen(argv[1]);
    if (len != 26)
    {
        printf("Key must contain 26 characters.\n");
        return 1;
    }

    for (int i = 0; i < len; i++)
    {
        if (!isalpha(argv[1][i]))
        {
            printf("All characters must be letters.\n");
            return 1;
        }

        for (int j = i + 1; j < len; j++)
        {
            if (argv[1][i] == argv[1][j])
            {
                printf("Key must not contain repeated letters.");
                return 1;
            }
        }
    }

    string plain = get_string("plaintext: ");
    printf("ciphertext: ");
    int plain_len = strlen(plain);

    for (int i = 0; i < plain_len; i++)
    {
        if (isupper(plain[i]))
        {
            printf("%c", toupper(argv[1][plain[i] - 65]));
        }
        else if (islower(plain[i]))
        {
            printf("%c", tolower(argv[1][plain[i] - 97]));
        }
        else
        {
            printf("%c", plain[i]);
        }
    }
    printf("\n");
}

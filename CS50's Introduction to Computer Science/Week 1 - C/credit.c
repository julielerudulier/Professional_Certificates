#include <cs50.h>
#include <math.h>
#include <stdio.h>

int every_other_digit(long card);
int MultiplyAndSum(int last_digit);
int number_of_digits(long card);
bool isValidAmex(long card, int numDigit);
bool isValidMastercard(long card, int numDigits);
bool isValidVisa(long card, int numDigits);

int main(void)
{
    long card = get_long("What's your credit card number? ");
    int sum_every_other_digit = every_other_digit(card);
    int numDigits = number_of_digits(card);
    bool amex = isValidAmex(card, numDigits);
    bool mcard = isValidMastercard(card, numDigits);
    bool visa = isValidVisa(card, numDigits);

    if (sum_every_other_digit % 10 != 0)
    {
        printf("INVALID\n");
        return 0;
    }
    else if (amex == true)
    {
        printf("AMEX\n");
    }
    else if (mcard == true)
    {
        printf("MASTERCARD\n");
    }
    else if (visa == true)
    {
        printf("VISA\n");
    }
    else
    {
        printf("INVALID\n");
        return 0;
    }
}

bool isValidAmex(long card, int numDigits)
{
    int first_two_digits = card / pow(10, 13);
    if ((numDigits == 15) && (first_two_digits == 34 || first_two_digits == 37))
    {
        return true;
    }
    else
    {
        return false;
    }
}

bool isValidMastercard(long card, int numDigits)
{
    int first_two_digits = card / pow(10, 14);
    if ((numDigits == 16) && (first_two_digits > 50 && first_two_digits <= 55))
    {
        return true;
    }
    else
    {
        return false;
    }
}

bool isValidVisa(long card, int numDigits)
{
    if (numDigits == 13)
    {
        int first_digit = card / pow(10, 12);

        if (first_digit == 4)
        {
            return true;
        }
    }
    else if (numDigits == 16)
    {
        int first_digit = card / pow(10, 15);

        if (first_digit == 4)
        {
            return true;
        }
    }
    return false;
}

int number_of_digits(long card)
{
    int count = 0;
    while (card > 0)
    {
        count++;
        card = card / 10;
    }
    return count;
}

int every_other_digit(long card)
{
    int sum = 0;
    bool isAlternateDigit = false;
    while (card > 0)
    {
        if (isAlternateDigit == true)
        {
            int last_digit = card % 10;
            int product = MultiplyAndSum(last_digit);
            sum = sum + product;
        }
        else
        {
            int last_digit = card % 10;
            sum = sum + last_digit;
        }
        isAlternateDigit = !isAlternateDigit;
        card = card / 10;
    }
    return sum;
}

int MultiplyAndSum(int last_digit)
{
    int multiply = last_digit * 2;
    int sum = 0;

    while (multiply > 0)
    {
        int last_digit_multiply = multiply % 10;
        sum = sum + last_digit_multiply;
        multiply = multiply / 10;
    }
    return sum;
}

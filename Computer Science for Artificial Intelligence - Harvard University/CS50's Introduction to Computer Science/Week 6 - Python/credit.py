from cs50 import get_int
import math

card = get_int("What's your credit card number? ")


def luhn(card):
    second_to_last_digits = []
    other_digits = []
    switch = True
    while card > 0:
        digit = card % 10
        if switch == True:
            other_digits.append(digit)
        elif switch == False:
            second_to_last_digits.append(digit)
        card /= 10
        card = math.trunc(card)
        switch = not switch

    sum_product = 0
    for i in second_to_last_digits:
        product = 2 * i
        if product >= 0 and product < 10:
            sum_product = sum_product + product
        elif product >= 10:
            sum_product = sum_product + (product % 10) + 1

    total_sum = 0
    for i in other_digits:
        total_sum = total_sum + i

    total_sum = total_sum + sum_product
    check = total_sum % 10
    return check


card_list = [int(x) for x in str(card)]
final_check = luhn(card)
length = len(str(card))

if length != 15 and length != 16 and length != 13:
    print("INVALID")

if (length == 15 and card_list[0] == 3) and (card_list[1] == 4 or card_list[1] == 7):
    if final_check == 0:
        print("AMEX")
else:
    print("INVALID")

if (
    length == 16
    and card_list[0] == 5
    and (
        card_list[1] == 1
        or card_list[1] == 2
        or card_list[1] == 3
        or card_list[1] == 4
        or card_list[1] == 5
    )
):
    if final_check == 0:
        print("MASTERCARD")
else:
    print("INVALID")

if (length == 16 or length == 13) and card_list[0] == 4:
    if final_check == 0:
        print("VISA")
else:
    print("INVALID")

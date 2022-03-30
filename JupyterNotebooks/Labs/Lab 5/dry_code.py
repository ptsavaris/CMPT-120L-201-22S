from typing import Tuple

SAVINGS = 0.15
CHECKINGS = 0.85


def addCheckings(numbers, transactions, checkings):
    for x in numbers:
        checkings += transactions[x]
    return checkings


def addSavings(numbers, transactions, checkings, savings):
    for x in numbers:
        checkings += transactions[x] * CHECKINGS
        savings += transactions[x] * SAVINGS
    return checkings, savings


def saturdays_bank_transactions(transations) -> Tuple[float, float]:
    savings = 1096.25
    checking = 1590.80

    checking = addCheckings([1, 2, 3, 6, 7, 8, 9, 10], transations, checking)
    checking, savings = addSavings([0, 4, 5], transations, checking, savings)

    return checking, savings


if __name__ == "__main__":
    transations = [
        300.00,
        -50.00,
        -5.00,
        -20,
        15.72,
        2083.93,
        -1034.00,
        -420.00,
        -5.23,
        -15.93,
        -72.90,
    ]
    new_balance = saturdays_bank_transactions(transations)
    print(
        "Your new checking balance is:",
        "${:.2f}".format(round(new_balance[0], 2)),
        "\nYour new savings balance is: ",
        "${:.2f}".format(round(new_balance[1], 2)),
    )
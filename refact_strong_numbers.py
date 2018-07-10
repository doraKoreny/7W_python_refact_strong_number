import math


def decide_strongness(comparable_number, compare_to):
    if comparable_number == compare_to:
        print("STRONG!!!!")
    else:
        print("NOT STRONG!!")


def strong_num(number):
    number = str(number)
    summa = 0
    for digit in range(len(number)):
        factorial_nums = math.factorial(int(number[digit]))
        summa += factorial_nums
    return summa


def main():
    number = 93
    summa = strong_num(number)
    decide_strongness(summa, number)


if __name__ == '__main__':
    main()

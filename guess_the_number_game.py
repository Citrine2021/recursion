import random
def GuessTheNumberGame(n, m):
    if n <= m:
        min_num = n
        max_num = m
    else:
        min_num = m
        max_num = n
    number = random.randint(min_num, max_num)
    inputNumber = int(input("Input a number you guess!\n"))

    for count in range(0, max_num - min_num):
        if inputNumber == number: return print("Correct!")
        inputNumber = int(input("Inccorect! Try again.\n"))
    return print("Incorrect! You faild...")

n, m = map(int, input("Input two numbers\n").split(','))
GuessTheNumberGame(n, m)
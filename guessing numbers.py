import random
ans = random.randint(1,10)
print('------------Guessing Number____________')
name = input("what is your name?")
n = str(name)
print("hi "+ n)
guess = 0
while guess !=ans:
    num = input("guess a number randomly ")
    guess = int(num)
    if guess == ans:
        print("well done ")
        print("but no prize")
    else:
        if guess > ans:
            print("Nope, too big")
        else:
            print("Nope too small")
print("Game Ended")

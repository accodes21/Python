import random
n = random.randint(1, 99)
x = 0
while x < 7:
    guess = int(input("Enter number between 1 and 99:"))
    x += 1
    if guess < n:
        print('Your guess is too low')
        print("Attempts left:",str(7-x))
    elif guess > n:
        print('Your guess is too high')
        print("Attempts left:",str(7-x))
    elif guess == n:
        break
if guess == n:
    print('You guessed the number in ' + str(x) + ' attempt!')
else:
    print('You did not guess the number, The number was ' + str(n))

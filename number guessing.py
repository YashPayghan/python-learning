import random
print("welcome to the number guessing game")
print("i choose number between 1 to 100")
num=random.randrange(1,100)
print(num)
def guess_no():
    lives=0
    difficulty = input("choose the dificulty (easy/hard)\n").lower()
    if difficulty == "easy":
        lives = 10
    elif difficulty == "hard":
        lives = 5
    print(f"You have {lives} lives.")
    while lives!=0  :
        user_guess = int(input("Enter your guess: "))
        if user_guess == num:
            print("you guess the no.")
            lives=0
        elif user_guess > num:
            if (user_guess-num) >= 10:
                print("too high")
                lives-=1
            elif (user_guess-num) <= 10:
                print("you are close")
                lives -= 1
        elif user_guess < num:
            if (num-user_guess) >=10:
                print("too low")
                lives -= 1
            elif (num-user_guess) <= 10:
                print("you are close")
                lives -= 1
    if lives==0 and user_guess!=num:
        print("you lost your all lives")
        print (f"your no is {num}")
guess_no()
replay=input("guess again").lower()
if replay=="yes":
    guess_no()
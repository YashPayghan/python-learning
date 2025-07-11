import random
def deal_card():
    cards=[11,2,3,4,5,6,7,8,9,10,10,10]
    card=random.choice(cards)
    return card
def calculate_score(cards):
   if sum(cards) == 21 and len(cards) == 2:
        return 0
   if 11 in cards and sum(cards) > 21:
       cards.remove(11)
       cards.append(1)
   return sum(cards)

def compare(user_score,computer_score):
    if user_score == computer_score:
        return"It's a tie!"
    elif computer_score==0:
        return"you lose computer have black jack"
    elif user_score==0:
        return "you win you have blackjack"
    elif computer_score==21:
        return "you lose"
    elif user_score==21:
        return "you win"
    elif user_score > 21:
        return "you lose"
    elif computer_score > 21:
        return "you win"
    elif user_score > computer_score:
        return "user win"
    else :
        return "You lose"
def play_game():
    user_card=[]
    computer_card=[]
    computer_score=-1
    user_score=-1
    is_game_over=False

    for _ in range(2):
        user_card.append(deal_card())
        computer_card.append(deal_card())
    while not is_game_over:
        users_score=calculate_score(user_card)
        computer_score=calculate_score(computer_card)
        print("Your card is:", user_card,"Your score is:", users_score)
        print("Computer card is:", computer_card[0])
        if users_score == 0 or computer_score == 0 or users_score>21:
            is_game_over=True
        else :
            do_you_want=input("type 'yes' to deal or 'no' to pass \n")
            if do_you_want == 'yes':
                user_card.append(deal_card())
            else:
                is_game_over=True

    while computer_score !=0 and computer_score<17:
        computer_card.append(deal_card())
        computer_score=calculate_score(computer_card)

    print("computer card is:",computer_card,"computer score is",computer_score)
    print(compare(user_score,computer_score))

while input("do you want to play the game of blackjack (yes/no)? \n") == "yes":
    print("\n"*20)
    play_game()
                    
                

               

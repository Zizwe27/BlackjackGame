from random import randint
from end_status import blackjack_or_bust
from value import card_value
from name import draw

def play_human_turn():
    total = 0
    give_card = 1
    card = ''
    while (give_card <= 2):
        card = randint(1,13)
        print(draw(card))
        value = card_value(card)
        total += value
        give_card += 1

    while (total < 21):
        move = input(f"You have {total}. Hit (y/n)? ")
        while (move != 'y' and move != 'n'):
            print("Sorry I didn't get that.")
            move = input(f"You have {total}. Hit (y/n)? ")

        if (move == 'y'):
            card = randint(1,13)
            print(draw(card))
            value = card_value(card)
            total += value
        elif(move == 'n'):
            break

    print(f"Final hand: {total}.")
    final_result = blackjack_or_bust(total)
    if(total >= 21):
        print(final_result)
from random import randint
from end_status import blackjack_or_bust
from value import card_value
from name import draw

def play_dealer_turn():
  total = 0
  give_card = 1
  card = ''
  while give_card <= 2:
    card = randint(1,13)
    print(draw(card))
    value = card_value(card)
    total += value
    give_card += 1

  while total < 17:
    print(f'Dealer has {total}.')
    card = randint(1,13)
    value = card_value(card)
    draw_current = draw(card)
    print(draw_current)
    total += value

  print(f'Final hand: {total}.')
  final = blackjack_or_bust(total)
  if total >= 21:
    print(final)
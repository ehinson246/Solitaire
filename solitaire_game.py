#!/usr/bin/env python3

import random

FULL_DECK_AMOUNT = 52
FIELD_CARD_AMOUNT = 28
STARTING_HAND_AMOUNT = 24
NUMBER_OF_FIELD_PILES = 7

def generate_fresh_deck():
    fresh_deck = []
    for n in range(FULL_DECK_AMOUNT):
        card = n + 1
        fresh_deck.append(card)
    return fresh_deck

def generate_shuffled_deck():
    shuffled_deck = []
    while len(shuffled_deck) < FULL_DECK_AMOUNT:
        random_number = random.randint(1, FULL_DECK_AMOUNT)
        if random_number not in shuffled_deck:
            shuffled_deck.append(random_number)
    return shuffled_deck

def get_starting_hand(deck):
    starting_hand = deck.copy()
    while len(starting_hand) > STARTING_HAND_AMOUNT:
        starting_hand.pop(0)
    return starting_hand

def get_field_cards(deck):
    field_cards = deck.copy()
    while len(field_cards) > FIELD_CARD_AMOUNT:
        field_cards.pop(-1)
    return field_cards

def create_field_piles(field_cards):
    pile_1 = []
    pile_2 = []
    pile_3 = []
    pile_4 = []
    pile_5 = []
    pile_6 = []
    pile_7 = []
    field_piles = [pile_1, pile_2, pile_3, pile_4, pile_5, pile_6, pile_7]
    pile_index = 0
    field_card_index = 0
    while pile_index < NUMBER_OF_FIELD_PILES:
        current_pile = field_piles[pile_index]
        pile_amount = pile_index + 1
        while len(current_pile) < pile_amount:
            next_card = field_cards[field_card_index]
            field_card_index += 1
            current_pile.append(next_card)
        pile_index += 1
    return field_piles

def deal_starting_position():
    deck = generate_shuffled_deck()
    starting_hand = get_starting_hand(deck)
    field_cards = get_field_cards(deck)
    field_piles = create_field_piles(field_cards)
    return (deck, starting_hand, field_cards, field_piles)

position = deal_starting_position()

deck = position[0]
starting_hand = position[1]
field_cards = position[2]
field_piles = position[3]

print(deck)
print(field_cards)
print(starting_hand)
print(field_piles)
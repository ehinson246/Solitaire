#!/usr/bin/env python3

import random
import copy

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
    starting_hand = copy.deepcopy(deck)
    while len(starting_hand) > STARTING_HAND_AMOUNT:
        starting_hand.pop(0)
    return starting_hand

def get_field_cards(deck):
    field_cards = copy.deepcopy(deck)
    while len(field_cards) > FIELD_CARD_AMOUNT:
        field_cards.pop(-1)
    return field_cards

def create_initial_field_piles(field_cards):
    pile_1 = []
    pile_2 = []
    pile_3 = []
    pile_4 = []
    pile_5 = []
    pile_6 = []
    pile_7 = []
    initial_field_piles = [pile_1, pile_2, pile_3, pile_4, pile_5, pile_6, pile_7]
    pile_index = 0
    field_card_index = 0
    while pile_index < NUMBER_OF_FIELD_PILES:
        current_pile = initial_field_piles[pile_index]
        pile_amount = pile_index + 1
        while len(current_pile) < pile_amount:
            next_card = field_cards[field_card_index]
            current_pile.append(next_card)
            field_card_index += 1
        pile_index += 1
    return initial_field_piles

def create_field_stacks(initial_field_piles):
    stack_1 = []
    stack_2 = []
    stack_3 = []
    stack_4 = []
    stack_5 = []
    stack_6 = []
    stack_7 = []
    field_stacks = [stack_1, stack_2, stack_3, stack_4, stack_5, stack_6, stack_7]
    index = 0
    for stack in field_stacks:
        pile_index = index
        top_card = initial_field_piles[pile_index][0]
        stack.append(top_card)
        index += 1
    return field_stacks

def finalize_field_piles(initial_field_piles):
    finalized_field_piles = copy.deepcopy(initial_field_piles)
    for pile in finalized_field_piles:
        pile.pop(0)
    return finalized_field_piles

def create_starting_position_info():
    deck = generate_shuffled_deck()
    starting_hand = get_starting_hand(deck)
    field_cards = get_field_cards(deck)
    initial_field_piles = create_initial_field_piles(field_cards)
    finalized_field_piles = finalize_field_piles(initial_field_piles)
    field_stacks = create_field_stacks(initial_field_piles)
    return (deck, starting_hand, field_cards, initial_field_piles, finalized_field_piles, field_stacks)

position = create_starting_position_info

deck = position[0]
starting_hand = position[1]
field_cards = position[2]
initial_field_piles = position[3]
finalized_field_piles = position[4]
field_stacks = position[5]

print(deck)
print(field_cards)
print(starting_hand)
print(initial_field_piles)
print(field_stacks)
print(finalized_field_piles)
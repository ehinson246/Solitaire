#!/usr/bin/env python3

import random
import copy

FULL_DECK_AMOUNT = 52
FIELD_CARD_AMOUNT = 28
STARTING_HAND_AMOUNT = 24
NUMBER_OF_FIELD_PILES = 7
DRAW_AMOUNT = 3

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
    placeholders = ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_']
    index = 0
    for stack in field_stacks:
        pile_index = index
        top_card = initial_field_piles[pile_index][0]
        stack.append(top_card)
        new_placeholders = copy.deepcopy(placeholders)
        stack.extend(new_placeholders)
        index += 1
    return field_stacks

def finalize_field_piles(initial_field_piles):
    finalized_field_piles = copy.deepcopy(initial_field_piles)
    for pile in finalized_field_piles:
        pile.pop(0)
    return finalized_field_piles

def create_visible_hand(starting_hand):
    visible_hand = []
    for card in starting_hand:
        card_visibility = (starting_hand.index(card) + 1) % DRAW_AMOUNT
        if card_visibility != 0:
            visible_hand.append('X')
        else:
            visible_hand.append(card)
    return visible_hand

def create_scoreboard():
    spades = []
    diamonds = []
    clubs = []
    hearts = []
    scoreboard = [spades, diamonds, clubs, hearts]
    return scoreboard

SPADES = 0
DIAMONDS = 1
CLUBS = 2
HEARTS = 3

def print_scoreboard(scoreboard):
    if len(scoreboard[SPADES]) == 0:
        spade_score = '0'
    else:
        spade_score = scoreboard[SPADES][-1]
    if len(scoreboard[DIAMONDS]) == 0:
        diamond_score = '0'
    else:
        diamond_score = scoreboard[DIAMONDS][-1]
    if len(scoreboard[CLUBS]) == 0:
        club_score = '0'
    else:
        club_score = scoreboard[CLUBS][-1]
    if len(scoreboard[HEARTS]) == 0:
        heart_score = '0'
    else:
        heart_score = scoreboard[HEARTS][-1]
    scoreboard_string = f'|{spade_score}|{diamond_score}|{club_score}|{heart_score}|'
    print(scoreboard_string)
    print("=========")
    
def print_piles_and_stacks(field_piles, field_stacks):
    row_1 = f'|{len(field_piles[0])}|{field_stacks[0][0]}|{field_stacks[0][1]}|{field_stacks[0][2]}|{field_stacks[0][3]}|{field_stacks[0][4]}|{field_stacks[0][5]}|{field_stacks[0][6]}|{field_stacks[0][7]}|{field_stacks[0][8]}|{field_stacks[0][9]}|{field_stacks[0][10]}|{field_stacks[0][11]}|{field_stacks[0][12]}|'
    row_2 = f'|{len(field_piles[1])}|{field_stacks[1][0]}|{field_stacks[1][1]}|{field_stacks[1][2]}|{field_stacks[1][3]}|{field_stacks[1][4]}|{field_stacks[1][5]}|{field_stacks[1][6]}|{field_stacks[1][7]}|{field_stacks[1][8]}|{field_stacks[1][9]}|{field_stacks[1][10]}|{field_stacks[1][11]}|{field_stacks[1][12]}|'
    row_3 = f'|{len(field_piles[2])}|{field_stacks[2][0]}|{field_stacks[2][1]}|{field_stacks[2][2]}|{field_stacks[2][3]}|{field_stacks[2][4]}|{field_stacks[2][5]}|{field_stacks[2][6]}|{field_stacks[2][7]}|{field_stacks[2][8]}|{field_stacks[2][9]}|{field_stacks[2][10]}|{field_stacks[2][11]}|{field_stacks[2][12]}|'
    print(row_1)

def print_current_position(scoreboard, field_piles, field_stacks, current_hand, visible_hand):
    print_scoreboard(scoreboard)
    print_piles_and_stacks(field_piles, field_stacks)
    # print_current_hand(current_hand)
    # print_visible_hand(visible_hand)

def initialize_solitaire_game():
    deck = generate_shuffled_deck()
    field_cards = get_field_cards(deck)
    initial_field_piles = create_initial_field_piles(field_cards)
    starting_hand = get_starting_hand(deck)
    
    scoreboard = create_scoreboard()
    field_piles = finalize_field_piles(initial_field_piles)
    field_stacks = create_field_stacks(initial_field_piles)
    current_hand = copy.deepcopy(starting_hand)
    visible_hand = create_visible_hand(starting_hand)

    while True:
        print_current_position()
        # play_turn()



deck = generate_shuffled_deck()
field_cards = get_field_cards(deck)
initial_field_piles = create_initial_field_piles(field_cards)



scoreboard = create_scoreboard()
field_piles = finalize_field_piles(initial_field_piles)
field_stacks = create_field_stacks(initial_field_piles)

print_scoreboard(scoreboard)
print_piles_and_stacks(field_piles, field_stacks)
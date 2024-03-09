#!/usr/bin/env python3

import random

def generate_fresh_deck():
    fresh_deck = []
    for i in range(52):
        card = i + 1
        fresh_deck.append(card)
    return fresh_deck

def generate_shuffled_deck():
    shuffled_deck = []
    while len(shuffled_deck) < 52:
        random_number = random.randint(1, 52)
        if random_number not in shuffled_deck:
            shuffled_deck.append(random_number)
    return shuffled_deck
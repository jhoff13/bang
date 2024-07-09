import random
import argparse
from prettytable import PrettyTable

bang_characters_descriptions = {
    "Bart Cassidy": "Each time he is hit, he draws a card.",
    "Black Jack": "He shows the second card he draws. If it is Hearts or Diamonds, he draws one more card.",
    "Calamity Janet": "She can use BANG! cards as Missed! cards and vice versa.",
    "El Gringo": "Each time he is hit by a player, he draws a random card from their hand.",
    "Jesse Jones": "He may draw his first card from the hand of any other player.",
    "Jourdonnais": "He has Barrel in play at all times; he can draw when he is the target of a BANG!.",
    "Kit Carlson": "He looks at the top 3 cards of the deck and chooses 2 to draw, discarding the other one.",
    "Lucky Duke": "He draws two cards for each draw! and chooses the best one.",
    "Paul Regret": "All players see him at a distance increased by 1.",
    "Pedro Ramirez": "He may draw his first card from the discard pile.",
    "Rose Doolan": "She sees all players at a distance decreased by 1.",
    "Sid Ketchum": "He may discard 2 cards to regain one life point.",
    "Slab the Killer": "Players need two Missed! cards to cancel his BANG! card.",
    "Suzy Lafayette": "As soon as she has no cards in her hand, she draws a card.",
    "Vulture Sam": "Whenever a player is eliminated from the game, he takes all the cards in that player's hand and in play.",
    "Willy the Kid": "He can play any number of BANG! cards."
}

def get_args():
    parser = argparse.ArgumentParser(description="Assign Bang Roles randomly to a group of players.")
    parser.add_argument('-p','--players', nargs='+', type=str, help='List of Player Names')
    args = parser.parse_args()
    return args

def assign_roles(players, characters):
    assert len(players) < len(characters), f"Error: There are more players than available characters! {len(players)} < {len(characters)}"

    # Shuffle the list of characters
    shuffled_characters = list(characters.keys())
    random.shuffle(shuffled_characters)

    # Assign characters to players
    assignments = {}
    for i, player in enumerate(players):
        character = shuffled_characters[i]
        assignments[player] = (character, characters[character])

    return assignments

def main():
    args = get_args()
    assignments = assign_roles(args.players, bang_characters_descriptions)

    table = PrettyTable()
    table.field_names = ["Player", "Character", "Description"]

    for player, (character, description) in assignments.items():
        table.add_row([player, character, description])
    print(table)

if __name__ == '__main__':
    main()

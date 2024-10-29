import math
from copy import copy
from typing import List, Tuple, Dict

def generate_valid_words(
        possible_words: List[str],
        letters_in_secret: List[Tuple[str, int]],
        letters_not_in_secret: List[str]
) -> List[str]:
    valid_words = []
    excluded_letters = set(letters_not_in_secret)

    for word in possible_words:
        if any(letter in excluded_letters for letter in word):
            continue

        valid = True
        for letter, position in letters_in_secret:
            if word[position] != letter:
                valid = False
                break

        if valid:
            valid_words.append(word)

    return valid_words

def generate_best_letters(
        possible_words: List[str],
        letters_not_played: List[str],
        letters_in_secret: List[Tuple[str, int]],
        letters_not_in_secret: List[str]
) -> str:
    total_possibilities: Dict[str, float] = {}
    num_possible_words = len(possible_words)

    for letter in letters_not_played:
        total_count = 0

        for secret_word in possible_words:
            if letter not in secret_word:
                continue

            filtered_words = generate_valid_words(
                possible_words,
                letters_in_secret + [(letter, secret_word.index(letter))],
                letters_not_in_secret
            )
            total_count += len(filtered_words)

        average_possibilities = total_count / num_possible_words if num_possible_words > 0 else 0
        total_possibilities[letter] = average_possibilities

    if total_possibilities:
        best_letter = max(total_possibilities, key=total_possibilities.get)
        worst_letter = min(total_possibilities, key=total_possibilities.get)
        return (f"Je te conseille : {best_letter} mais pas : {worst_letter}")
    else:
        return ""

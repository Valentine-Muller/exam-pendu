import math
from typing import List, Tuple, Dict

def generate_valid_words(
        possible_words: List[str],
        letters_in_secret: List[Tuple[str, int]],
        letters_not_in_secret: List[str]
) -> List[str]:
    valid_words = []
    excluded_letters = set(letters_not_in_secret)

    for word in possible_words:
        # Skip words containing excluded letters
        if any(letter in excluded_letters for letter in word):
            continue

        valid = True
        for letter, position in letters_in_secret:
            # Check if the letter at the given position matches the expected letter
            if position < len(word) and word[position] != letter:
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

    # Iterate over letters that have not been played yet
    for letter in letters_not_played:
        total_count = 0

        for secret_word in possible_words:
            # Count only if the letter is in the current word
            if letter not in secret_word:
                continue

            # Generate valid words by including the current letter
            filtered_words = generate_valid_words(
                possible_words,
                letters_in_secret + [(letter, secret_word.index(letter))],
                letters_not_in_secret
            )
            total_count += len(filtered_words)

        # Calculate the average number of valid words for the current letter
        average_possibilities = total_count / num_possible_words if num_possible_words > 0 else 0
        total_possibilities[letter] = average_possibilities

    # Determine the best and worst letters based on calculated possibilities
    if total_possibilities:
        sorted_letters = sorted(total_possibilities.items(), key=lambda x: x[1], reverse=True)

        best_letter = sorted_letters[0][0]
        worst_letter = sorted_letters[-1][0] if len(sorted_letters) > 1 else None

        top_suggestions = sorted_letters[:3]

        # Prepare the suggestion message
        suggestions = ', '.join([f"{letter} ({score:.1f})" for letter, score in top_suggestions])

        return f"Je te conseille : {suggestions}."
    else:
        return "Aucune suggestion disponible."


# Exemple d'utilisation
possible_words = ["apple", "angle", "grape", "peach"]
letters_not_played = ["a", "e", "g"]
letters_in_secret = [("a", 1)]
letters_not_in_secret = ["p"]

result = generate_best_letters(possible_words, letters_not_played, letters_in_secret, letters_not_in_secret)
print(result)

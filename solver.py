import math
from copy import copy
from collections import Counter


def generate_valid_words(
    possible_words: list[str],
    letters_in_secret: list[tuple[str, int]],
    letters_not_in_secret: list[str]
) -> list[str]:

    valid_words = []

    for word in possible_words:
        # Exclure les mots contenant des lettres interdites
        if any(letter in word for letter in letters_not_in_secret):
            continue

        # Vérifier que les lettres bien placées correspondent
        if all(word[pos] == letter for letter, pos in letters_in_secret):
            valid_words.append(word)

    return valid_words



def generate_best_letters(
    possible_words: list[str],
    letters_not_played: list[str],
    letters_in_secret: list[tuple[str, int]],
    letters_not_in_secret: list[str]
) -> str:

    # Compter les occurrences de chaque lettre dans les mots restants
    letter_counts = Counter()

    for word in possible_words:
        # Ajouter les lettres uniques de chaque mot
        letter_counts.update(set(word))

    # Filtrer les lettres déjà jouées ou exclues
    for letter in letters_not_in_secret + [ltr for ltr, _ in letters_in_secret]:
        if letter in letter_counts:
            del letter_counts[letter]

    # Calculer la fréquence moyenne pour chaque lettre restante
    total_words = len(possible_words)
    letter_frequencies = {
        letter: count / total_words
        for letter, count in letter_counts.items()
    }

    # Trouver la lettre avec la fréquence moyenne la plus élevée
    best_letter = max(letter_frequencies, key=letter_frequencies.get, default="")
    return best_letter











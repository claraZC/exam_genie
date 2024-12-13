import pytest

from solver import generate_valid_words
from generate_dicts import lire_filtrer_mots


# test fonction lire_filtrer_mots
def test_lire_filtrer_mots_accents_et_tirets():
    """
    Teste que les mots avec des accents, des espaces ou des tirets sont correctement filtrés.
    """
    fichier_test = "tests/data_test/filetest1.txt"
    result = lire_filtrer_mots(fichier_test, 6)
    # mots attendus
    expected = ['ECOUTE', 'ARRETE', 'CAMION']
    assert result == expected


def test_generate_valid_words_start_d():
    """On sait que la première lettre du mot est un D"""
    assert generate_valid_words(
        possible_words=["DEVANT", "ENTREE", "PORTER", "GAUCHE"],
        letters_in_secret=[('D', 0)],
        letters_not_in_secret=[]
    ) == ["DEVANT"]
    


def test_generate_valid_words_empty_possible_words():
    """
    Teste que la fonction retourne une liste vide si possible_words est vide.
    """
    possible_words = []
    letters_in_secret = [('D', 0)]  
    letters_not_in_secret = []
    result = generate_valid_words(possible_words, letters_in_secret, letters_not_in_secret)
    # reultat attendu : liste vide, car possible_words est vide
    assert result == []
    
    
# test_generate_valid_words.py
import pytest
from solver import generate_valid_words

def test_generate_valid_words_with_excluded_and_present_letters():
    """
    Teste que la fonction exclut les mots contenant des lettres exclues et respecte les lettres présentes.
    """
    possible_words = ["DEVANT", "ENTREE", "PORTER", "GAUCHE"]
    letters_in_secret = [('D', 0)]  
    letters_not_in_secret = ['E', 'T']   
    result = generate_valid_words(possible_words, letters_in_secret, letters_not_in_secret)
    # Résultat attendu : les mots contenant 'E' et 'T' sont exclus
    expected = ["DEVANT", "PORTER"]  #
    assert result == expected




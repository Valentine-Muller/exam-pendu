import pytest
from solver import generate_valid_words

def test_generate_valid_words_start_d():
    assert generate_valid_words(
        possible_words=["DEVANT", "ENTREE", "PORTER", "GAUCHE"],
        letters_in_secret=[('D', 0)],
        letters_not_in_secret=[]
    ) == ["DEVANT"]

def test_possible_words_vide():
    assert generate_valid_words([], letters_in_secret=[], letters_not_in_secret=[]) == []

def test_aucune_lettre_jouee():
    possible_words = ["DEVANT", "ENTREE", "PORTER"]
    assert generate_valid_words(possible_words, letters_in_secret=[], letters_not_in_secret=[]) == possible_words

def test_lettres_exclues_et_presentes():
    assert generate_valid_words(
        possible_words=["DEVANT", "ENTREE", "PORTER"],
        letters_in_secret=[('E', 1)],
        letters_not_in_secret=[('R', 2)]
    ) == ["ENTREE"]

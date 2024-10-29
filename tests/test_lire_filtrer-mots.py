import pytest
from generate_dicts import lire_filtrer_mots

def test_fichier_vide():
    with pytest.raises(ValueError, match="Le fichier est vide"):
        lire_filtrer_mots("tests/data_test/fichier_vide.txt")

def test_filtre_longueur():
    result = lire_filtrer_mots("tests/data_test/mots.txt", longueur=6)
    assert result == ["exemple"]  # Remplacez par les mots attendus

def test_exclusion_accents():
    result = lire_filtrer_mots("tests/data_test/mots.txt", longueur=6)
    assert "café" not in result
    assert "maison" not in result  # Vérifiez que les mots avec espaces ou tirets sont exclus

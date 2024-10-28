"""
Depuis le fichier liste_mots.txt, on récupère tous les mots de 6,7,8,9,10 lettres.
et on génère 5 fichiers textes contenant les mots en fonction de leur taille (un mot par ligne, séparé par un \n):
dico_6_lettres.txt
dico_7_lettres.txt
dico_8_lettres.txt
dico_9_lettres.txt
dico_10_lettres.txt
On enlève les accents, les espaces, les tirets et les mots en double.
"""

import unicodedata

def lire_filtrer_mots(chemin_lexique, longueur):
    mots_uniques = set()

    with open(chemin_lexique, 'r', encoding='utf-8') as fichier:
        for ligne in fichier:
            for mot in ligne.split():
                mot_nettoye = mot.replace('-', '')
                mot_nettoye = mot_nettoye.strip()
                mot_nettoye = ''.join(c for c in mot_nettoye if not c.isspace())
                mot_nettoye = unicodedata.normalize('NFKD', mot_nettoye)
                mot_nettoye = mot_nettoye.encode('ASCII', 'ignore').decode('utf-8')

                if len(mot_nettoye) == longueur and not any(char.isdigit() for char in mot_nettoye):
                    mots_uniques.add(mot_nettoye.upper())

    return sorted(mots_uniques)

def ecrire_liste_mots(liste_mots:list, longueur:int) -> None:
    """Génère un fichier texte contenant tous les mots pour une longueur donné"""

    chemin_dico_ecriture:str = f"data/dico_{longueur}_lettres.txt"

    with open(chemin_dico_ecriture, 'w', encoding='utf-8') as file:
        file.writelines(f"{mot}\n" for mot in liste_mots)




def main(chemin:str) -> None:
    for long in range(6,11):
        # génère la liste de mot pour la longueur donné
        lst_mots = lire_filtrer_mots(chemin_lexique=chemin, longueur=long)

        # Génère un fichier texte correspondant
        ecrire_liste_mots(lst_mots, longueur=long)

if __name__ == '__main__':
    chemin = "data/liste_mots.txt"
    main(chemin= chemin)
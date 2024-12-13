import unicodedata

def lire_filtrer_mots(chemin_lexique, longueur):
    import unicodedata

def lire_filtrer_mots(chemin_lexique: str, longueur: int) -> list[str]:

    mots_valides = set()
    mots_trop_longs = set()

    with open(chemin_lexique, 'r', encoding='utf-8') as file:
        for ligne in file:
            # Extraire uniquement le premier mot (avant les espaces)
            mot = ligne.split()[0]

            # Nettoyer le mot
            mot = ''.join(
                c for c in unicodedata.normalize('NFD', mot) 
                if unicodedata.category(c) != 'Mn'
            )
            mot = mot.replace('-', '').replace(' ', '').upper()

            # Filtrer selon la longueur
            if len(mot) == longueur:
                mots_valides.add(mot)
            elif len(mot) > longueur:
                mots_trop_longs.add(mot)

    # Écrire les mots trop longs dans un fichier "trop_gros.txt"
    with open("trop_gros.txt", 'w', encoding='utf-8') as file:
        file.writelines(f"{mot}\n" for mot in sorted(mots_trop_longs))

    return sorted(mots_valides)

    return []


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

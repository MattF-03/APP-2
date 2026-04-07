import copy   # On importe copy permettant de copier des objets sans modifier l'original
import time   # On importe time permettant de mesurer le temps d'exécution
import APP_datasets 

def tri_insertion(avions, policy):
    liste = copy.deepcopy(avions)   # On crée une copie indépendante de la liste avions pour ne pas la modifier pendant le tri 

    nombre_comparaisons = 0    # On initialise un compteur pour mesurer le nombre de comparaisons effectuées

    for i in range(1, len(liste)):   # On parcourt la liste à partir du deuxième élément car le premier est considéré comme trié
        avion_courant = liste[i]   # On mémorise l'avion à insérer à sa bonne place dans la partie déjà triée
        j = i - 1   # On part de l'avion juste à gauche de l'avion courant pour remonter vers le début

        while j >= 0:
            nombre_comparaisons += 1
            if policy(avion_courant, liste[j]):   # Si l'avion courant est plus prioritaire que l'avion en position j
                liste[j + 1] = liste[j]   # On décale l'avion en position j d'une case vers la droite pour libérer de la place
                j -= 1   # On recule d'une position pour continuer à remonter vers le début
            else:
                break   

        liste[j + 1] = avion_courant   # On insère l'avion courant à la position libérée

    return liste, nombre_comparaisons

def tri_selection(avions, policy):
    liste = copy.deepcopy(avions)   # On crée une copie indépendante de la liste avions pour ne pas la modifier pendant le tri 

    nombre_comparaisons = 0   

    for i in range(len(liste) - 1):
        identifiant_prioritaire = i   # On suppose que l'avion le plus prioritaire est celui en position i

        for j in range(i + 1, len(liste)):   # On parcourt tous les avions qui n'ont pas encore été placés
            nombre_comparaisons += 1
            if policy(liste[j], liste[identifiant_prioritaire]):   # Si l'avion en position j est plus prioritaire que celui trouvé jusqu'ici
                identifiant_prioritaire = j   # On a trouvé un avion plus prioritaire

        liste[i], liste[identifiant_prioritaire] = liste[identifiant_prioritaire], liste[i]   # On échange l'avion le plus prioritaire trouvé avec celui en position i

    return liste, nombre_comparaisons

def comparer(avions, policy, nom = ""):
    temps_0 = time.perf_counter()   # On retourne le temps écoulé en secondes depuis un point de référence
    liste_triee_selection, nombre_selection = tri_selection(avions, policy)   # On trie les avions par sélection et on récupère la liste triée et le nombre de comparaisons
    temps_1 = time.perf_counter()   # On note l'heure de fin du tri sélection
    liste_triee_insertion, nombre_insertion = tri_insertion(avions, policy)   # On trie les mêmes avions par insertion et on récupère la liste triée et le nombre de comparaisons
    temps_2 = time.perf_counter()   # On note l'heure de fin du tri insertion pour pouvoir calculer sa durée

    duree_selection = (temps_1 - temps_0) * 1000   # On calcule la durée du tri sélection en soustrayant les deux temps et en convertissant en millisecondes
    duree_insertion = (temps_2 - temps_1) * 1000   # On calcule la durée du tri insertion en soustrayant les deux temps et en convertissant en millisecondes

    print("  [{:<13}]   Nom = {:<4}  Sélection = {:<5} ({:.3f} ms)   Insertion = {:<5} ({:.3f} ms)".format(nom, len(avions), nombre_selection, duree_selection, nombre_insertion, duree_insertion))
    # On affiche sur une ligne le nom du scénario, la taille de la liste, le nombre de comparaisons de la liste et le temps d'exécution de la liste

if __name__ == "__main__":   # On vérifie que le fichier est exécuté directement et non importé
    from policies import POLICIES, policy_crise   # On importe le dictionnaire de toutes les policies et la policy crise depuis policies.py
    from generateur import GENERATEURS

    print("\n=== ORDRE D'ATTERRISSAGE ===\n")   # On affiche le titre de la section avec une ligne vide avant et après
    for nom, policy in POLICIES.items():   # On parcourt chaque policy du dictionnaire en récupérant son nom et sa fonction
        avions_tries, liste_triee_insertion = tri_insertion(APP_datasets.AVIONS_INITIAL, policy)   # On trie les avions selon la policy et on récupère la liste triée et le nombre de comparaisons
        for i in avions_tries[:6]:   # On parcourt les 6 premiers avions de la liste triée (les 6 prioritaires)
            print("  {} | {}".format(nom, i["id"]))   # On affiche le nom de la policy et l'identifiant de l'avion correspondant
        
        print()

    print("\n=== COMPARAISON sélection VS insertion ===\n")   # On affiche le titre de la section avec une ligne vide avant et après
    for nom, policy in POLICIES.items():
        comparer(APP_datasets.AVIONS_INITIAL, policy, nom)   # On appelle la fonction comparer qui affiche le nombre de comparaisons et le temps d'exécution tri_insertion et tri_selection

    print("\n=== TEST PERFORMANCE (policy_crise) ===\n")   # On affiche le titre de la section avec une ligne vide avant et après
    for n in [10, 30, 50, 100]:   # On teste quatre tailles de trafic différentes pour observer l'évolution des performances
        comparer(GENERATEURS["chaos"](n), policy_crise, "Crise n = {}".format(n))   # On génère un trafic chaotique de n avions et on compare tri_insertion et tri_selection avec la policy crise
    print()
 

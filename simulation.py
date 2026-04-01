import copy   # On importe copy permettant de copier des objets sans modifier l'original
from tri import tri_insertion   # On importe la fonction tri_insertion depuis le fichier tri.py
from APP_datasets import AVIONS_INITIAL

def simuler(avions, policy, nom = "", afficher = True):
# On définit une fonction de simulation prenant une liste d'avions, une policy choisie pour les atterrissages, un nom pour la simulation et l'affichage affiché par défaut
    file = copy.deepcopy(avions)   # On crée une copie indépendante de la liste avions pour ne pas la modifier pendant la simulation
    
    sauves = []   # On crée les listes des avions sauvés
    crashes = []   # On crée les listes des avions crashés

    tour = 0   # On crée un compteur s'incrémentant à chaque fois qu'un avion atterrit

    while len(file) > 0:   # On répète la boucle tant qu'il reste des avions en attente
        tour += 1   # On incrémente le compteur de tours à chaque itération

        for i in file:   # On parcourt chaque avion de la file
            i["fuel"] -= 1   # On diminue le carburant de chaque avion de 1

        morts = []   # On crée une liste vide pour stocker les avions qui vont se crasher
        survivants = []   # On crée une liste vide pour stocker les avions encore en vie

        for j in file:   # On parcourt chaque avion pour les séparer selon leur carburant
            if j["fuel"] <= 0:   # Si l'avion n'a plus de carburant, alors il se crashe
                morts.append(j)   # On ajoute l'avion à la liste des morts
            else:   
                survivants.append(j)   # On ajoute l'avion à la liste des survivants

        file = survivants   # On remplace la file par uniquement les avions survivants

        for k in morts:  # On parcourt chaque avion crashé
            crashes.append(k)   # On ajoute l'avion crashé à la liste des crashes
            if afficher:  
                print(f"  Tour {tour} | CRASH : {i["id"]}")   # On affiche le numéro du tour et l'identifiant de l'avion crashé

        if len(file) == 0:   # Si tous les avions se sont crashés
            break

        file = tri_insertion(file, policy)[0]   # On trie les avions selon la policy choisie
        atterri = file.pop(0)   # On retire le premier avion de la file car il va atterrir
        sauves.append(atterri)   # On ajoute l'avion atterri à la liste des sauvés

        if afficher:   
            print(f"  Tour {tour} | OK : {atterri["id"]}  Carburant = {atterri["fuel"]}  En attente = {len(file)}")  # On affiche les informations de l'atterrissage

    taux = len(sauves) / len(avions) * 100   # On calcule le pourcentage d'avions sauvés
    print(f"  --- {nom} | Sauvés = {len(sauves)}  Crashés = {len(crashes)}  Taux = {taux:.1f}%")   # On affiche le bilan de la simulation
    return {"sauves": sauves, "crashes": crashes, "taux": taux}   # On retourne un dictionnaire contenant les résultats

def comparer_policies(avions, policies):   # On définit une fonction qui compare plusieurs policies d'atterrissage
    bilans = []   # On crée une liste vide pour stocker les résultats de chaque policy
    for nom, policy in policies.items():   # On parcourt chaque policy du dictionnaire policies
        bilan = simuler(avions, policy, afficher = False)   # On simule les atterrissages sans affichage
        bilan["nom"] = nom   # On ajoute le nom de la policy au bilan
        bilans.append(bilan)   # On ajoute le bilan à la liste des bilans

    bilans.sort(key = lambda b: len(b["crashes"]))   # On trie les bilans par nombre de crashes croissant

    print("\n=== Policy  |  Sauvés  |  Crashés  |  Taux ===")   # On affiche l'en-tête du tableau de comparaison
    for bilan in bilans:   # On parcourt chaque bilan
        print(f"{bilan["nom"]}  {len(bilan["sauves"])}  {len(bilan["crashes"])}  {bilan["taux"]:.1f}%")   # On affiche les résultats de chaque policy

if __name__ == "__main__":   # On vérifie que le fichier est exécuté directement et non importé
    from policies import POLICIES, policy_crise   # On importe les policies depuis le fichier policies.py

    print("\n=== SIMULATION ===\n")   # On affiche le titre de la simulation
    simuler(AVIONS_INITIAL, policy_crise, "crisis")   # On lance la simulation avec la policy de crise

    print("\n=== COMPARAISON DES POLICIES ===\n")   # On affiche le titre de la comparaison
    comparer_policies(AVIONS_INITIAL, POLICIES)   # On lance la comparaison de toutes les policies

    print()

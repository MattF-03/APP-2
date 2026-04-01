import copy   # On importe la bibliothèque copy permettant de copier des objets sans modifier l'original
from APP_datasets import AVIONS_INITIAL
from policies import POLICIES, policy_crise
from tri import tri_insertion, comparer
from generateur import GENERATEURS

DUREE_ATTERRISSAGE = 3   # On considère que chaque avion prend 3 minutes pour se poser

def simuler(avions_initiaux, policy):   # On définit une fonction qui va simuler les atterrissages selon une policy précise.
    file_attente = copy.deepcopy(avions_initiaux)   # On crée une copie indépendante de la liste des avions pour ne pas modifier les données d'origine

    sauves = []   # On crée les listes des avions sauvés
    crashes = []   # On crée les listes des avions crashés

    while file_attente:   # On lance une boucle qui continue tant qu'il reste au moins un avion en vol
        file_attente, nombre_comparaisons = tri_insertion(file_attente, policy)   # On réorganise la file d'attente selon la policy choisie pour décider qui passe en premier
        sauves.append(file_attente.pop(0))   # On fait atterrir le premier avion de la liste et on l'ajoute aux sauvés

        survivants = []   # On crée une liste temporaire pour les avions qui ont encore assez de carburant pour attendre

        for avion in file_attente:
            avion["fuel"] -= DUREE_ATTERRISSAGE   # On retire 3 minutes de carburant à l'avion car il a dû attendre pendant que le précédent atterrissait
            if avion["fuel"] == 0:   # On vérifie si le réservoir de l'avion est vide 
                crashes.append(avion)   # On ajoute l'avion à la liste des crashes
            else:
                survivants.append(avion)   # On ajoute l'avion à la liste des survivants
        file_attente = survivants   # On met à jour la file d'attente en ne gardant que les avions qui ne se sont pas crashés

    return sauves, crashes

if __name__ == "__main__":   # On vérifie que le fichier est exécuté directement et non importé
    print("-" * 40)   # On crée une ligne de tirets pour rendre le texte plus lisible

    print("\n=== 1. ORDRE D'ATTERRISSAGE PAR POLICY ===")
    for nom, policy in POLICIES.items():   # On parcourt le dictionnaire POLICIES en récupérant à chaque tour le nom de la policy et la fonction associée
        resultat, tests = tri_insertion(AVIONS_INITIAL, policy)   # On trie la liste de départ selon la policy actuelle et on récupère le nombre de vérifications effectuées
        top_6 = [avion["id"] for avion in resultat[:6]]   # On crée une liste contenant les identifiants des 6 prochains avions à atterrir   
        print(f"  Policy : {nom:15}")   # On affiche le nom de la policy de priorité utilisée
        print(f"  Calculs : {tests}")   # On affiche le nombre d'opérations que l'ordinateur a dû faire pour trier les avions
        print(f"  Ordre : {top_6}")   # On affiche la liste des 6 avions prioritaires
        print("-" * 30)   # On crée une ligne de tirets pour rendre le texte plus lisible

    print("\n=== 2. COMPARAISON selection VS insertion ===")
    for nom, policy in POLICIES.items():
        comparer(AVIONS_INITIAL, policy, nom)   # On définit une fonction qui mesure et affiche les performances entre le tri par insertion et le tri par sélection

    print("\n=== 3. TEST PERFORMANCE (scénario chaos, policy crise) ===")
    for n in [10, 30, 50, 100]:   # On crée une boucle pour tester des groupes d'avions de plus en plus grands
        comparer(GENERATEURS["chaos"](n), policy_crise, "Chaos n = {}".format(n))   # On teste l'efficacité du tri dans une situation de chaos avec n avions

    print("\n=== 4. SIMULATION (Durée atterrissage = {} min) ===".format(DUREE_ATTERRISSAGE))
    print("  {:^18} | {:^6} | {:^6}".format("Policy", "Sauvés", "Crashés"))   # On affiche l'en-tête du tableau avec les titres des colonnes 
    print("  " + "-" * 40)   # On met des tirets pour séparer les titres du tableau
    for nom, policy in POLICIES.items():
        sauves, crashes = simuler(AVIONS_INITIAL, policy)   # On lance la simulation d'atterrissage et on récupère les listes d'avions sauvés et crashés
        print("  {:^18} | {:^6} |  {:^6}".format(nom, len(sauves), len(crashes)))   # On affiche le nom de la policy et le nombre total d'avions sauvés et crashés

    print("\n=== 5. SIMULATION PAR SCENARIO ===")
    print("  {:^22} | {:^6} | {:^6}".format("Scénario", "Sauvés", "Crashés"))   # On affiche l'en-tête du second tableau avec les titres des colonnes pour comparer les différents types de trafic
    print("  " + "-" * 44)   # On met des tirets pour séparer les titres du tableau
    for nom, generateur in GENERATEURS.items():   # On parcourt chaque type de situation pour voir leur impacte sur les vols
        sauves, crashes = simuler(generateur(24), policy_crise)   # On crée 24 avions pour le scénario actuel et on les fait atterrir selon la policy de crise
        print("  {:^22} | {:^6} |  {:^6}".format(nom, len(sauves), len(crashes)))   # On affiche le bilan final pour chaque scénario testé
    print()

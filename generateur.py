import random

PREFIXES = ["AF", "LH", "BA", "EK", "IB", "UA", "QR", "TK", "AC", "DL", "AZ", "EY", "SU"]
# "Air_France", "Lufthansa", "British_Airways", "Emirates", "Iberia", "United_Airlines", "Qatar_Airways", "Turkish_Airlines", "Air_Canada", "Delta_Airlines", "Azerbaijan_Airlines", "Etihad_Airways", "Aeroflot_Russian_Airlines "

def index(i):
    return "{}{}".format(PREFIXES[i % len(PREFIXES)], 100 + (i * 7) % 900) 
        # On veut trouver un index périodique dans la liste PREFIXES
        # On génère un numéro entre 100 et 999 qui change à chaque avion afin d'avoir un identifiant

def avion_info(i, carburant, medical, technique, diplomatique_niv):
    return {
        "index": index(i),   # Identifiant généré 
        "carburant": carburant,   # Carburant passé en paramètre
        "medical": medical,   # Urgence militaire 
        "technique": technique,   # Urgence technique
        "diplomatique_niv": diplomatique_niv,   # Niveau d'importance diplomatique du vol   
        "temps_arrivee": round(19.40 + i * 0.02, 3)   # On calcule l'heure d'arrivée prévue de chaque avion  
    }

def generer_normal(nombre, valeur_initiale = 42):
    random.seed(valeur_initiale)   # On veut fixer la valeur initiale pour reproduire les résultats
    avions = []
    for i in range(nombre):
        carburant = random.randint(15, 60)   # Carburant entre 15 et 60 minutes = pas de situatuation critique 
        medical = random.random() < 0.05   # 5% de chance d'urgence médicale
        technique = random.random() < 0.05   # 5% de chance d'incident technique
        diplomatique_niv = random.randint(1, 3)   # Niveau d'importance diplomatique bas (1 à 3) 

        avions.append(avion_info(i, carburant, medical, technique, diplomatique_niv))   # On ajoute le dictionnaire retourné par avion_info à la liste avions
    return avions

def generer_crise_carburant(nombre, valeur_initiale = 1):
    random.seed(valeur_initiale)
    avions = []
    for i in range(nombre):
        if random.random() < 0.7:   # 70% des avions ont peu de carburant
            carburant = random.randint(5, 20)   # Carburant critique
        else:
            carburant = random.randint(21, 50)   # Carburant correct
    
        medical = random.random() < 0.05   
        technique = random.random() < 0.05   
        diplomatique_niv = random.randint(1, 3)   

        avions.append(avion_info(i, carburant, medical, technique, diplomatique_niv))   
    return avions

def generer_crise_medicale(nombre, valeur_initiale = 2):
    random.seed(valeur_initiale)
    avions = []
    for i in range(nombre):
        carburant = random.randint(10, 55)   # Carburant entre 10 et 55 minutes = pas de situatuation critique
        medical = random.random() < 0.4   # 40% des avions ont une urgence médicale à bord
        technique = random.random() < 0.05   
        diplomatique_niv = random.randint(1, 3)   

        avions.append(avion_info(i, carburant, medical, technique, diplomatique_niv))   
    return avions

def generer_sommet_diplomatique(nombre, valeur_initiale = 3):
    random.seed(valeur_initiale)
    avions = []
    for i in range(nombre):
        carburant = random.randint(15, 60)   # Carburant entre 15 et 60 minutes = pas de situatuation critique
        medical = random.random() < 0.05   
        technique = random.random() < 0.05   

        if random.random() < 0.6:   # 60% des avions transportent une délégation officielle (niveau 4 ou 5)
            diplomatique_niv = random.randint(4, 5)   # Chef d'État ou personnalité de haut rang
        else:
            diplomatique_niv = random.randint(1, 3)   # Vol commercial ordinaire

        avions.append(avion_info(i, carburant, medical, technique, diplomatique_niv))   
    return avions

def generer_chaos(nombre, valeur_initiale = 99):
    random.seed(valeur_initiale)
    avions = []
    for i in range(nombre):
        carburant = random.randint(5, 60)   # Carburant variable 
        medical = random.random() < 0.2   # 20% des avions ont une urgence médicale
        technique = random.random() < 0.15   # 15% des avions ont un incident technique
        diplomatique_niv = random.randint(1, 5)   # Tous les niveaux possibles

        avion = avion_info(i, carburant, medical, technique, diplomatique_niv)
        avion["index"] = "CH{:03d}".format(i)   
        # On écrase l'identifiant généré par index() pour le remplacer par un identifiant afin d'identifier facilement que cet avion vient du scénario chaos

        avions.append(avion)
    return avions

GENERATEURS = {
    "normal": generer_normal,
    "carburant": generer_crise_carburant,
    "medical": generer_crise_medicale,
    "diplomatique": generer_sommet_diplomatique,
    "chaos": generer_chaos,
}

def afficher_stats(avions, nom):
    med = 0   # On compte le nombre d'avions ayant une urgence médicale à bord
    for i in avions:
        if i["medical"]:
            med += 1

    tech = 0   # On compte le nombre d'avions ayant un incident technique
    for i in avions:
        if i["technique"]:
            tech += 1

    carb = 0   # On compte le nombre d'avions avec un carburant critique (10 minutes ou moins)
    for i in avions:
        if i["carburant"] <= 10:
            carb += 1

    diplo = 0   # On compte le nombre d'avions avec un niveau d'importance diplomatique élevé (4 ou 5)
    for i in avions:
        if i["diplomatique_niv"] >= 4:
            diplo += 1

    total_carburant = 0   # On calcule le carburant moyen de tous les avions
    for i in avions:
        total_carburant = total_carburant + i["carburant"]
    moy = total_carburant / len(avions)

    print("  {:<15} | {:>6} avions | prob_medical = {:<3} prob_technique = {:<3} carburant_critique = {:<3} niv_diplomatique = {:<3} | moy_carburant = {:.1f} min".format(nom, len(avions), med, tech, carb, diplo, moy))
    # On affiche toutes les statistiques sur une seule ligne

if __name__ == "__main__":
    print("\n=== GENERATEUR DE TRAFIC ===\n")
    for taille in [10, 24, 50, 100]:   # On teste 4 tailles différentes de trafic
        print("--- nombre = {} ---".format(taille))   # On affiche le nombre d'avions testé
        for nom, gen in GENERATEURS.items():
            afficher_stats(gen(taille), nom)
        print()
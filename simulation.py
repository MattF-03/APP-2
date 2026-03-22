def simulation(liste_avion_trier):

    temps = 0
    avions_sauve = []
    avions_crash = []

    print(f"\n--- Début de la simulation (19h42) ---")

    while len(liste_avion_trier) > 0:
        avion = liste_avion_trier.pop(0)       #récupération de l'avion de plus important 

#Vérification 
        if avion['carburant'] <= 0:
            crashs += 1
            print(f"[T+{temps}min] !!! CRASH !!! : Le vol {avion['index']} s'est écrasé.")
        else:
            sauves += 1
            print(f"[T+{temps}min] Atterrissage : {avion['index']} (Fuel restant: {avion['carburant']} min)")

# plus le temps passe, plus le carburant part
        temps += 1
        for a in liste_avion_triee:
            a['carburant'] -= 1
    
    print(f"\n=== BILAN FINAL ===")
    print(f"Avions sauvés : {sauves}")
    print(f"Crashs : {crashs}")
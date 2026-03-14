import copy
from tri import tri_insertion
from APP_datasets import AVIONS_INITIAL


def simuler(avions, policy, nom = "", verbose = True):
    """Simule les atterrissages : 1 avion/tour, fuel--, crash si fuel<=0."""
    file = copy.deepcopy(avions)
    sauves, crashes, tour = [], [], 0

    while file:
        tour += 1
        for a in file: a["fuel"] -= 1
        crashs = [a for a in file if a["fuel"] <= 0]
        file   = [a for a in file if a["fuel"] > 0]
        for a in crashs:
            crashes.append(a)
            if verbose: print("  Tour {:>3} | CRASH : {}".format(tour, a["id"]))
        if not file: break
        file, _ = tri_insertion(file, policy)
        atterri = file.pop(0)
        sauves.append(atterri)
        if verbose:
            flags = ("[MED]" if atterri.get("medical") else "") + ("[TECH]" if atterri.get("technical_issue") else "")
            print("  Tour {:>3} | OK : {:>6} {:6} fuel={:>3}  en attente={}".format(
                tour, atterri["id"], flags, atterri["fuel"], len(file)))

    taux = len(sauves) / len(avions) * 100
    print("  --- {} | sauves={} crashes={} taux={:.1f}%".format(
        nom, len(sauves), len(crashes), taux))
    return {"sauves": sauves, "crashes": crashes, "taux": taux}


def comparer_policies(avions, policies):
    """Compare toutes les policies sur le meme trafic."""
    bilans = []
    for nom, p in policies.items():
        b = simuler(avions, p, nom=nom, verbose=False)
        b["nom"] = nom
        bilans.append(b)
    bilans.sort(key = lambda b: b["crashes"].__len__())
    print("\n  {:<15} {:>8} {:>9} {:>10}".format("Policy","Sauves","Crashes","Taux"))
    for b in bilans:
        print("  {:<15} {:>8} {:>9} {:>9.1f}%".format(
            b["nom"], len(b["sauves"]), len(b["crashes"]), b["taux"]))


if __name__ == "__main__":
    from policies import POLICIES, policy_crisis

    print("\n=== SIMULATION — policy crisis (24 avions) ===\n")
    simuler(AVIONS_INITIAL, policy_crisis, nom="crisis", verbose=True)

    print("\n=== COMPARAISON DES POLICIES ===\n")
    comparer_policies(AVIONS_INITIAL, POLICIES)
from APP_datasets import AVIONS_INITIAL
from policies import POLICIES, policy_crisis
from tri import comparer
from generateur import GENERATEURS
from simulation import simuler, comparer_policies

print("\n=== 1. VALIDATION ===")
print("  {} avions  med={}  tech={}  fuel_min={}".format(
    len(AVIONS_INITIAL),
    sum(1 for a in AVIONS_INITIAL if a["medical"]),
    sum(1 for a in AVIONS_INITIAL if a["technical_issue"]),
    min(a["fuel"] for a in AVIONS_INITIAL)))

print("\n=== 2. COMPARAISON TRIS ===")
for nom, p in POLICIES.items(): comparer(AVIONS_INITIAL, p, nom)

print("\n=== 3. SIMULATION ===")
simuler(AVIONS_INITIAL, policy_crisis, nom="crisis", verbose = True)
comparer_policies(AVIONS_INITIAL, POLICIES)

print("\n=== 4. STRESS TESTS ===")
for n in [10, 30, 50, 100]: comparer(GENERATEURS["chaos"](n), policy_crisis, "n={}".format(n))
for nom, gen in GENERATEURS.items(): simuler(gen(50), policy_crisis, nom = nom, verbose=False)

print("\n=== 5. EVENEMENT IMPRÉVU ===")
def policy_must_land(a1, a2):
    if a1.get("must_land") != a2.get("must_land"): return bool(a1.get("must_land"))
    return policy_crisis(a1, a2)
simuler(AVIONS_INITIAL + [{"id":"EMRG01","fuel":5,"medical":True,"technical_issue":True,
    "diplomatic_level":5,"arrival_time":99.99,"must_land":True}],
    policy_must_land, nom = "must_land", verbose = True)
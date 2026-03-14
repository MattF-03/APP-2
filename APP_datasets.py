avions = [
    {"index": "AF342", "carburant": 18, "medical": False, "technique": False, "diplomatique_niv": 2},
    {"index": "LH908", "carburant": 25, "medical": False, "technique": True,  "diplomatique_niv": 1},
    {"index": "BA117", "carburant": 14, "medical": True,  "technique": False, "diplomatique_niv": 3},
    {"index": "EK202", "carburant": 40, "medical": False, "technique": False, "diplomatique_niv": 5},
    {"index": "AZ721", "carburant": 9,  "medical": False, "technique": False, "diplomatique_niv": 1}
]

AVIONS_INITIAL = [
    {"index": "AF342", "carburant": 18, "medical": False, "technique": False, "diplomatique_niv": 2, "temps_arrivee": 19.42},
    {"index": "LH908", "carburant": 25, "medical": False, "technique": True,  "diplomatique_niv": 1, "temps_arrivee": 19.44},
    {"index": "BA117", "carburant": 14, "medical": True,  "technique": False, "diplomatique_niv": 3, "temps_arrivee": 19.46},
    {"index": "EK202", "carburant": 40, "medical": False, "technique": False, "diplomatique_niv": 5, "temps_arrivee": 19.47},
    {"index": "IB455", "carburant": 12, "medical": False, "technique": False, "diplomatique_niv": 2, "temps_arrivee": 19.49},
    {"index": "AZ721", "carburant": 9, "medical": False, "technique": False, "diplomatique_niv": 1, "temps_arrivee": 19.50},
    {"index": "UA331", "carburant": 22, "medical": False, "technique": False, "diplomatique_niv": 4, "temps_arrivee": 19.51},
    {"index": "QR998", "carburant": 16, "medical": False, "technique": False, "diplomatique_niv": 5, "temps_arrivee": 19.52},
    {"index": "TK876", "carburant": 8, "medical": False, "technique": False, "diplomatique_niv": 2, "temps_arrivee": 19.53},
    {"index": "AC410", "carburant": 35, "medical": False, "technique": False, "diplomatique_niv": 3, "temps_arrivee": 19.54},
    {"index": "DL550", "carburant": 11, "medical": True, "technique": False, "diplomatique_niv": 2, "temps_arrivee": 19.55},
    {"index": "SU119", "carburant": 27, "medical": False, "technique": False, "diplomatique_niv": 1, "temps_arrivee": 19.56},
    {"index": "SN204", "carburant": 6, "medical": False, "technique": False, "diplomatique_niv": 2, "temps_arrivee": 19.57},
    {"index": "KL330", "carburant": 19, "medical": False, "technique": False, "diplomatique_niv": 3, "temps_arrivee": 19.58},
    {"index": "EY601", "carburant": 28, "medical": False, "technique": False, "diplomatique_niv": 4, "temps_arrivee": 19.59},
    {"index": "AF118", "carburant": 15, "medical": False, "technique": True, "diplomatique_niv": 2, "temps_arrivee": 20.00},
    {"index": "LH332", "carburant": 21, "medical": False, "technique": False, "diplomatique_niv": 1, "temps_arrivee": 20.01},
    {"index": "BA450", "carburant": 10, "medical": False, "technique": False, "diplomatique_niv": 3, "temps_arrivee": 20.02},
    {"index": "IB900", "carburant": 17, "medical": False, "technique": False, "diplomatique_niv": 2, "temps_arrivee": 20.03},
    {"index": "AZ333", "carburant": 13, "medical": False, "technique": False, "diplomatique_niv": 1, "temps_arrivee": 20.04},
    {"index": "UA870", "carburant": 24, "medical": False, "technique": False, "diplomatique_niv": 4, "temps_arrivee": 20.05},
    {"index": "QR555", "carburant": 7, "medical": False, "technique": False, "diplomatique_niv": 5, "temps_arrivee": 20.06},
    {"index": "TK221", "carburant": 20, "medical": False, "technique": False, "diplomatique_niv": 2, "temps_arrivee": 20.07},
    {"index": "AC990", "carburant": 5, "medical": False, "technique": False, "diplomatique_niv": 3, "temps_arrivee": 20.08},
]


avions_diplomatic_50 = [
    {"index": f"DP{i:02}",
     "carburant": 10 + (i % 30),
     "medical": False,
     "technique": False,
     "diplomatique_niv": 4 + (i % 2),
     "temps_arrivee": 19.40 + i * 0.01}
    for i in range(50)
]

avions_diplomatic_50 = [
    {"index": f"DP{i:02}",
     "carburant": 10 + (i % 30),
     "medical": False,
     "technique": False,
     "diplomatique_niv": 4 + (i % 2),
     "temps_arrivee": 19.40 + i * 0.01}
    for i in range(50)
]

import random

avions_chaos_100 = []

for i in range(100):
    avions_chaos_100.append({
        "index": f"CH{i:03}",
        "carburant": random.randint(5, 60),
        "medical": random.random() < 0.2,
        "technique": random.random() < 0.15,
        "diplomatique_niv": random.randint(1, 5),
        "temps_arrivee": 19.40 + i * 0.005
    })

import networkx as nx

G = nx.Graph()

"""
G.add_edge("A", "B", weight=4)
G.add_edge("B", "D", weight=2)
G.add_edge("A", "C", weight=3)
G.add_edge("C", "D", weight=4)
nx.shortest_path(G, "A", "D", weight="weight")
['A', 'B', 'D']
"""

fichier = open("graphe.json", "r")

taches = fichier.readlines()

num = ""
predecesseur = ""
duree = ""

for n, tache in enumerate(taches):

    G.add_edge(num, predecesseur, weight=duree)

fichier.close()
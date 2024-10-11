import networkx as nx
import matplotlib.pyplot as plt
import json

#initialisation d'un nouveau graphe
G = nx.DiGraph()

#lecture du fichier json
fichier = open("graphe.json", "r")
taches = json.load(fichier)

num = ""
predecesseur = ""
duree = ""

#pour chaque tâche du projet
for tache in range(len(taches)):
    #on récupère le numéro et la durée de la tâche
    num = taches[tache]["num"]
    duree = taches[tache]["duree"]

    #si plusieurs prédecesseurs
    if (len(taches[tache]["predecesseur"]) > 1):
        predecesseurs = taches[tache]["predecesseur"]
        for i in range(len(predecesseurs)):
            #ajout d'un segment au graphe
            G.add_edge(predecesseurs[i], num, weight=duree)

    #si pas de prédecesseur (cas de la première tâche)
    elif (taches[tache]["predecesseur"][0] == 0):
        continue

    else:
        predecesseur = taches[tache]["predecesseur"][0]
        #ajout d'un segment au graphe
        G.add_edge(predecesseur, num, weight=duree)

#ajout de τ
G.add_edge(len(taches)-1, len(taches))

#dessin du graphe
pos = nx.shell_layout(G)
nx.draw(G, pos, with_labels=True, arrows=True, node_size=700, node_color="skyblue")
edge_labels = nx.get_edge_attributes(G, "weight")
nx.draw_networkx_edge_labels(G, pos, edge_labels)

plt.show()


fichier.close()
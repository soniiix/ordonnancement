import networkx as nx
import matplotlib.pyplot as plt
import json

def chercherDuree(taches, predecesseur):
    for tache in taches :
        if tache["num"] == predecesseur:
            return tache['duree']

#initialisation d'un nouveau graphe
G = nx.DiGraph()

#lecture du fichier json
fichier = open("graphe.json", "r")
taches = json.load(fichier)

#pour chaque tâche du projet
for tache in range(len(taches)):
    #on récupère le numéro de la tâche
    num = taches[tache]["num"]

    #si plusieurs prédecesseurs
    if (len(taches[tache]["predecesseur"]) > 1):
        predecesseurs = taches[tache]["predecesseur"]
        for i in range(len(predecesseurs)):
            duree = chercherDuree(taches, predecesseurs[i])
            #ajout d'un segment au graphe
            G.add_edge(predecesseurs[i], num, weight=duree)

    #si pas de prédecesseur (cas de la première tâche)
    elif (taches[tache]["predecesseur"][0] == 0):
        continue

    else:
        predecesseur = taches[tache]["predecesseur"][0]
        duree = chercherDuree(taches, predecesseur)
        #ajout d'un segment au graphe
        G.add_edge(predecesseur, num, weight=duree)

#ajout de τ
duree = chercherDuree(taches, len(taches))
G.add_edge(len(taches), len(taches)+1, weight=duree)


#position topologique des éléments
for layer, nodes in enumerate(nx.topological_generations(G)):
    for node in nodes:
        G.nodes[node]["layer"] = layer
pos = nx.multipartite_layout(G, subset_key="layer")
#dessin du graphe
nx.draw(G, pos, with_labels=True, arrows=True, node_size=700, node_color="skyblue")
#ajout de l'affichage de la durée des tâches
edge_labels = nx.get_edge_attributes(G, "weight")
nx.draw_networkx_edge_labels(G, pos, edge_labels)

plt.show()


fichier.close()
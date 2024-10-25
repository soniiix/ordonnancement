import networkx as nx
import matplotlib.pyplot as plt
import json

#fonction pour chercher la durée de la tâche précédente
def chercher_duree(taches, predecesseur):
    for tache in taches :
        if tache["num"] == predecesseur:
            return tache['duree']

#initialisation d'un nouveau graphe
G = nx.DiGraph()

#lecture du fichier json
fichier = open("data.json", "r")
taches = json.load(fichier)

#pour chaque tâche du projet
for tache in taches:
    #on récupère le numéro de la tâche
    num = tache["num"]

    #on évite le cas de la première tâche (pas de prédécesseur)
    if tache["predecesseur"][0] != 0:

        #si plusieurs prédecesseurs
        if (len(tache["predecesseur"]) > 1):
            predecesseurs = tache["predecesseur"]
            for predecesseur in predecesseurs:
                duree = chercher_duree(taches, predecesseur)
                #ajout d'un segment au graphe
                G.add_edge(predecesseur, num, weight=duree)

        #si un seul prédécesseur
        else:
            predecesseur = tache["predecesseur"][0]
            duree = chercher_duree(taches, predecesseur)
            #ajout d'un segment au graphe
            G.add_edge(predecesseur, num, weight=duree)

#ajout de τ, la tâche finale
duree = chercher_duree(taches, len(taches))
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


#sauvegarde du graphe
plt.savefig("graphe.png")

plt.show()


fichier.close()
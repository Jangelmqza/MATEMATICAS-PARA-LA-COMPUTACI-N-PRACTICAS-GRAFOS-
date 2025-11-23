import networkx as nx 
G=nx.Graph() #Creamos un grafo vacio

nx.draw_shell(G, with_labels = True) #Grafica el grafo

G.add_node(1) 
G.add_node('a')
G.add_nodes_from ([2,3,4])

nx.draw_shell (G, with_labels=True)


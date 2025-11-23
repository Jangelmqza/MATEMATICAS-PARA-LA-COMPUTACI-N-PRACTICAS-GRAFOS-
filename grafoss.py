import networkx as nx 
import scipy
import matplotlib.pyplot as plt

G=nx.Graph() #Creamos un grafo vacio

G.add_node(1) #agregamos un vertice nombre 1
G.add_node('a') #vertice nombre a
G.add_nodes_from ([2,3,4]) #agrefamos una lista de vertices

G.add_edge(1,2)#arista que conecta 1 y 2
G.add_edges_from([(1,3), (1,4)]) #lista de aristas
G.add_edge(1,1)#bucle
G.add_edge(2,1)#(1,2) y (2,1) son la misma arista

print("El numero de nodos es: ", G.number_of_nodes())
print("El numero de aristas es: ", G.number_of_edges())

print("los vertices son: ", G.nodes)
print("las aristas son: ",G.edges)

nx.draw_shell (G, with_labels=True)     
plt.show()
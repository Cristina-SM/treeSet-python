import networkx as nx

def build_digraph_with_weights():
    
    # Añade aqui la rutina que hiciste en el primer ejercicio
    # de esta semana para crear el grafo dirigido con pesos.
    first_line = input().split()
    num_nodes  = int(first_line[0])
    num_edges  = int(first_line[1])

    # Paso 1: Crear grafo direcional con num_nodes
    DG = nx.DiGraph()
    # Paso 2: Añadir los vértices del grafo
    for i in range(1, num_nodes+1):
        DG.add_node(i)

    for i in range(num_edges):
        entrante = input().split()
        first = int(entrante[0])
        second = int(entrante[1])
        w = int(entrante[2])
        DG.add_edge(first, second, weight=w)
    return DG

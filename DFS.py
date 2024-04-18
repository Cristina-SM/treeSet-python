import networkx as nx
from simple_stack import *

def dfs_topological_sort(graph):
    """
    Compute one topological sort of the given graph.
    """
    
    # La solucion que retorna esta función es un diccionario de Python.
    #   * La clave del diccionario es el número del nodo
    #   * El valor es el orden topologico asignado a ese nodo
    # 
    # Por ejemplo, si tenemos el siguiente grafo dirigido con 3 vertices:
    #                    3 ---> 2 ---> 1
    # ... el orden topologico es:
    #                El vértice 3 va en la primera posición
    #                El vértice 2 en la segunda posición
    #                El vértice 1 en la tercera posición
    # Con lo que debemos devolver un diccionario con este contenido:
    #     {1: 3, 2: 2, 3: 1}

    N = graph.number_of_nodes()

    
    visibleNodes = set()  # En este ejercicio utilizamos un set
                          # para recordar los nodos visibles
    order = {}

    # solve it here! ------------------------------------------------


    def dfs_iterative(u):
        q = Stack()
        nonlocal N
        q.push(u)
        while not q.isEmpty():
            u = q.peek()
            visibleNodes.add(u)
            for w in graph.successors(u):
                if w not in visibleNodes:
                    visibleNodes.add(w)
                    q.push(w)
            if u == q.peek():
                u = q.pop()
                order[u] = N
                N = N - 1
        return

    #  2. Añade código también aqui
    #  ... for
    for node in graph.nodes():
        if node not in visibleNodes:
            dfs_iterative(node)

    return order

def longitud(graph):
    return graph.number_of_nodes()
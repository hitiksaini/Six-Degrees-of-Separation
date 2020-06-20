import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
 #facebook node is dwonloaded named facebook_combined.txt and saved it the same directory
    
graph=nx.read_edgelist("facebook_combined.txt")
N=list(graph.nodes())   #making a graph object and capturing all nodes from edgelist

shortest_path_length_list=[]  #finding shortest 

for u in N:
    for v in N:
        if u!=v:   #for finding shortest for different nodes
            l=nx.shortest_path_length(graph,u,v)
            print(" shortest path between ",u, " and ", v," is ", l)
            shortest_path_length_list.append(l)
            
min_spl=min(shortest_path_length_list)
max_spl=max(shortest_path_length_list)
avg_spl=np.average(shortest_path_length_list)

print("Minimum shortest path lenght: ", min_spl)
print("Maximum shortest path lenght: ", max_spl)
print("Average shortest path lenght: ", avg_spl)

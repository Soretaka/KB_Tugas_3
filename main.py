from node import Node
from graph import Graph

graph = Graph()

bandar_lampung = Node('Bandar Lampung', 629)
jakarta = Node('Jakarta', 446)
bogor = Node('Bogor', 421)
bandung = Node('Bandung', 320)
cirebon = Node('Cirebon', 246)
tasikmalaya = Node('Tasikmalaya', 248)
purwokerto = Node('Purwokerto', 132)
cilacap = Node('Cilacap', 156)
semarang = Node('Semarang', 108)
yogyakarta = Node('Yogyakarta', 0)

graph.add_edge(bandar_lampung, jakarta, 233)
graph.add_edge(jakarta, bogor, 56)
graph.add_edge(jakarta, cirebon, 219)
graph.add_edge(bogor, bandung, 124)
graph.add_edge(bandung, cirebon, 129)
graph.add_edge(bandung, tasikmalaya, 111)
graph.add_edge(tasikmalaya, cilacap, 144)
graph.add_edge(cirebon, cilacap, 170)
graph.add_edge(cirebon, purwokerto, 146)
graph.add_edge(cirebon, semarang, 234)
graph.add_edge(cilacap, purwokerto, 50)
graph.add_edge(cilacap, yogyakarta, 172)
graph.add_edge(purwokerto, yogyakarta, 168)
graph.add_edge(semarang, yogyakarta, 130)

gbfs_cost, gbfs_path = graph.gbfs(bandar_lampung, yogyakarta)
a_star_cost, a_star_path = graph.a_star(bandar_lampung,yogyakarta)

print("gbfs cost: " + str(gbfs_cost))
print("a star cost: " + str(a_star_cost))
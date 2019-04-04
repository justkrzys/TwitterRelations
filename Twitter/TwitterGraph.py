import pandas
import networkx as nx
import numpy

#Opens the twitter file
twitter = open('twitter_cleaned.csv',encoding='ISO-8859-1')
file = pandas.read_csv(twitter)

#Graph is drawn using the two columns from the twitter_cleaned.csv file
g = nx.Graph()
g.add_nodes_from(file['a'])
g.add_nodes_from(file['b'])
g.add_edges_from(file.values)

print(g.number_of_edges())
print(g.number_of_nodes())

#The degree and centrality of the data of the graph is determined and printed
degree_data = pandas.Series(dict(nx.degree(g)))
degree_data = degree_data.sort_values(ascending=False)

print(degree_data.head(10))

log10data = numpy.log10(degree_data)

cent = pandas.Series(nx.degree_centrality(g))
cent = cent.sort_values(ascending=False)

print(cent.head(10))

#The grah is cored so that the number of nodes displayed is not too much for the computer to handle
g_cored = nx.k_core(g,3)
print(g_cored.number_of_edges())
print(g_cored.number_of_nodes())

cored_degree_data = pandas.Series(dict(nx.degree(g_cored)))
cored_degree_data = cored_degree_data.sort_values(ascending=False)

#Labels each node according to its name in the twitter_cleaned.csv file
labels_dict = {}

for node in g_cored.nodes():
    if type(node) == str:
        if len(node)>=15:
            labels_dict[node] = node[:13] + '.'
        else:
            labels_dict[node] = node

#Draws the graph and displays it   
nx.draw(g_cored, with_labels=True, labels=labels_dict, font_size=8)


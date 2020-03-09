

class Graph:
    # input for dijkstra algorithm as a list of dictionary objects as defined in the assignment #2-A
    # each dictionary contains fields: r1, r2, which represents the two routers connected by a link, and cost,
    # representing the cost of the link
    linkStateList = [{'r1': 'u', 'r2': 'v', 'cost': 2}, {'r1': 'v', 'r2': 'w', 'cost': 3},
                     {'r1': 'v', 'r2': 'x', 'cost': 2},
                     {'r1': 'u', 'r2': 'x', 'cost': 1}, {'r1': 'u', 'r2': 'w', 'cost': 5},
                     {'r1': 'x', 'r2': 'w', 'cost': 3},
                     {'r1': 'x', 'r2': 'y', 'cost': 1}, {'r1': 'w', 'r2': 'y', 'cost': 1},
                     {'r1': 'w', 'r2': 'z', 'cost': 5},
                     {'r1': 'y', 'r2': 'z', 'cost': 2}]

    # initialize empty adjacency list
    adjacencyList = [[] for i in range(ord('z') + 1)]

    # constructor populates adjacencyList with all the links in the linkStateList
    def __init__(self):
        self.addEdges(self.linkStateList)

    # function to add edges to the adjacency list
    def addEdges(self, linkStateList):
        for link in linkStateList:
            # get routers from link object
            r1 = link["r1"]
            r2 = link["r2"]
            #add link to adjacency list for both r1 and r2 (since router topology is undirected Graph)
            self.adjacencyList[ord(r1)].append(link)
            self.adjacencyList[ord(r2)].append(link)

class Dijkstra:

    def __init__(self):

# main function
if __name__ == "__main__":
    # create graph that contains adjacency list needed for djikstra
    graph = Graph()
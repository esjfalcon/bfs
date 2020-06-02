from queue import Queue

graph = {
    'A' : ['B','S'],
    'B' : ['A'],
    'C' : ['D','E','F','S'],
    'D' : ['C'],
    'E' : ['C','H'],
    'F' : ['C','G'],
    'G' : ['F','S'],
    'H' : ['E','G'],
    'S' : ['A','C','G']
}

def bfs(sn, en, graph):
        parent ={}
        visited ={}
        queue = Queue()


        for i in graph.keys():
                visited[i] = False


        list=[]

        s=sn #source node
        visited[s] = True #source node mark as visited
        parent[s] = None #there is no parent of source node
        queue.put(s)

        while not queue.empty():
                u = queue.get()
                list.append(u)

                for i in graph[u]:
                        if not visited[i]:
                                visited[i] = True #if the child of a node not visisted mark it as visited
                                parent[i] = u
                                queue.put(i)


        j=en #end node
        path=[]
        while j is not None:
                path.append(j)
                j = parent[j]

        path.reverse()
        print(path)

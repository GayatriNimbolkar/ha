import collections
from collections import defaultdict
print("let's create a graph")
g = defaultdict(list)
print("enter the number of nodes in graph")
n = int(input())
for j in range(1, n+1):
    if j == 1:
        root = eval(input("enter root i.e 1st node"))
        r = root
    else:

        r = eval(input("enter the " + str(j) + " node"))
    g[r] = []
    adj_n = int(input("enter the number of child adjacent to " + str(j) +" node"))
    for i in range(1, adj_n+1):
        print("enter the "+str(i) + " child adjacent to "+str(r)+ " node")
        nod = eval(input())
        g[r].append(nod)
print("your graph is:")
print(g)
visited=set()

def bfs(graph, root,goal):
    visited, queue = set(), collections.deque([root])
    visited.add(root)
    while queue:
        vertex = queue.popleft()
        print(str(vertex) + " ", end="")
        if vertex != goal:
            for neighbour in graph[vertex]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    queue.append(neighbour)
        else:
            queue = []

goal = eval(input("Enter goal node"))
bfs(g, root,goal)
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

def dfs(g,visited, root,goal):
    visited.add(root)
    print(root, end=' ')
    for neighbour in g[root]:
        if neighbour != goal:
            if neighbour not in visited:
                dfs(g, visited, neighbour,goal)
        else:
            print(goal)
            break
        
goal = eval(input("Enter goal node"))
dfs(g,visited, root,goal)
from sys import maxsize as INFINITY

TEMPORARY = 1
PERMANENT = 2

class Vertex:
        def __init__(self, name):
           self.name = name

          
class UndirectedWeightedGraph:

        def __init__(self,size=20):
           self._adj = [  [0 for column in range(size)]  for row in range(size) ]
           self._n = 0
           self._vertexList = []
           

       
        def numVertices(self):
            return self._n


        def numEdges(self):  
            e = 0
            for i in range(self._n):
                for j in range(i):
                    if self._adj[i][j]!=0:
                        e+=1
            return e


        def vertices(self):
            return [vertex.name for vertex in self._vertexList]


        def edges(self):  
            edges = []
            for i in range(self._n):
                for j in range(i):
                   if self._adj[i][j] != 0:
                      edges.append( (self._vertexList[i].name, self._vertexList[j].name, self._adj[i][j]) )
            return edges


        def _getIndex(self,s):
            index = 0
            for name in (vertex.name for vertex in self._vertexList):
                if s == name:
                   return index
                index += 1
            return None


        def insertVertex(self,name):
            if name in (vertex.name for vertex in self._vertexList): 
                print("Vertex with this name already present in the graph")
                return                
            self._vertexList.append( Vertex(name) )  
            self._n += 1


        def removeVertex(self,name):
             u = self._getIndex(name)
             if u is None:
                print("Vertex not present in the graph")
                return
        
             self._adj.pop(u)

             for i in range(self._n):
                  self._adj[i].pop(u)
                  
             self._vertexList.pop(u)
             self._n -= 1
               
    
        def insertEdge(self, s1, s2, w):
            u = self._getIndex(s1)
            v = self._getIndex(s2)
            if u is None:
                print("First vertex not present in the graph")
            elif v is None:
                print("Second vertex not present in the graph")
            elif u == v:
                print("Not a valid edge") 
            elif self._adj[u][v] != 0 :
                print("Edge already present in the graph") 
            else:  
                self._adj[u][v] = w
                self._adj[v][u] = w
                
        
        def removeEdge(self, s1,s2):
             u = self._getIndex(s1)
             v = self._getIndex(s2)
             if u is None:
                print("First vertex not present in the graph")
             elif v is None:
                print("Second vertex not present in the graph")
             elif self._adj[u][v] == 0:
                print("Edge not present in the graph")
             else:        
                self._adj[u][v] = 0
                self._adj[v][u] = 0


        def isAdjacent(self, s1, s2):
            u = self._getIndex(s1)
            v = self._getIndex(s2)
            if u is None:
                print("First vertex not present in the graph")
                return False
            elif v is None:
                print("Second vertex not present in the graph")
                return False
            return False if self._adj[u][v] == 0 else True   

      
        def degree(self,s):
        
            u = self._getIndex(s)
            if u is None:
               print("Vertex not present in the graph")
               return

            deg = 0
            for v in range(self._n):
                if self._adj[u][v] != 0 :
                     deg += 1
            return deg

        def prims(self):
            edgesInTree = 0
            wtTree = 0
                            
            for v in range(self._n):
                 self._vertexList[v].status = TEMPORARY
                 self._vertexList[v].length = INFINITY
                 self._vertexList[v].predecessor = None

            root = 0
            self._vertexList[root].length = 0
                
            while True:
                c = self._tempVertexMinL()
        
                if c == None:
                     if edgesInTree == self._n-1:
                          print("Weight of minimum spanning tree is", wtTree)
                     else:
                          print("Graph is not connected, Spanning tree not possible")
                     return         
                
                self._vertexList[c].status = PERMANENT
                        
                # Include edge ( self._vertexList[c].predecessor,c ) in the tree
                if c != root:
                     edgesInTree += 1
                     p=self._vertexList[c].predecessor
                     print("(" ,self._vertexList[p].name, "," , self._vertexList[c].name, ")","Weight :",self._adj[p][c] )
                     wtTree = wtTree + self._adj[self._vertexList[c].predecessor][c]
                        
                for v in range(self._n):
                   if self._adj[c][v] and self._vertexList[v].status == TEMPORARY:
                        if self._adj[c][v] < self._vertexList[v].length:
                            self._vertexList[v].length = self._adj[c][v]
                            self._vertexList[v].predecessor = c
                        

        def _tempVertexMinL(self):
            min = INFINITY
            x = None
        
            for v in range(self._n):
               if self._vertexList[v].status == TEMPORARY and self._vertexList[v].length < min :
                   min = self._vertexList[v].length
                   x = v
            return x
        

if __name__ == '__main__':

   g = UndirectedWeightedGraph()
   n=int(input("Enter the number of vertex :"))
   while n>0 :
    v=input("Enter the vetex :")
    g.insertVertex(v)
    n=n-1
   
   ch=input("Do you want to add edges ?(y/n)")
   while ch=='y':
    fv=input("Enter first vertex :")
    sv=input("Enter second vertex :")
    e=int(input("Enter cost of the edge :"))
    g.insertEdge(fv,sv,e)
    ch=input("Do you want to add edges ?(y/n)")
   
 

   g.prims()
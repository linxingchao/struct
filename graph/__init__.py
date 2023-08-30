from queue import Queue

#无向图
class Graph:
    def __init__(self,v:int):
        self._v = v #顶点个数
        self._adj = {}
        self._found = False
        
        for i in range(v):
            self._adj[i] = []
            
    def add_edge(self,s,t):
        self._adj[s].append(t)
        self._adj[t].append(s)
        
    #广度优先,s为起点，t为终点，求s到t的最短路径    
    def bfs(self,s,t):
        if s == t:
            return
        
        visited = [False]*self._v
        visited[s] = True
        queue = Queue()
        queue.put(s)
        prev = [-1]*self._v
        
        while queue.qsize() != 0:
            w = queue.get()
            for i in range(len(self._adj[w])):
                q = self._adj[w][i]
                if not visited[q]:
                    prev[q] = w
                    if q == t:
                        Graph.show_info(prev,s,t)
                        return
                    visited[q] = True
                    queue.put(q)
    
    #深度优先                
    def dfs(self,s,t):
        self._found = False
        visited = [False]*self._v
        prev = [-1]* self._v
        self._recurDfs(s,t,visited,prev)
        Graph.show_info(prev,s,t)
    
    def _recurDfs(self,w,t,visted:list,prev:list):
        if self._found:
            return
        visited[w] = True
        if w == t:
            self._found = True
            return
        
        for i in len(self._adj[w]):
            q = self._adj[w][i]
            if not visted[q]:
                prev[q] = w
                self._recurDfs(q,t,visted,prev)
                    
    @staticmethod                
    def show_info(prev,s,t):
        if prev[t] != -1 and t != s:
            Graph.show_info(prev,s,prev[t])
        print(str(t) + " ")
        
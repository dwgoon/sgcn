
class GraphEngine:
    
    def __init__(self, pkg):
        pkg = pkg.lower()
        if pkg not in ["igraph", "networkx"]:
            raise ValueError("Unsupported graph package: %s"%(pkg))
    
        self._pkg = pkg

    def create_fileio(self):
        if self._pkg == "networkx":
            from sgcn.fileio import NetworkxIO
            return NetworkxIO(self)
        elif self._pkg == "igraph":
            from sgcn.fileio import IgraphIO
            return IgraphIO(self)        
        else:
            raise RuntimeError("[SYSTEM] should not be reached here...")
                               
    
    def create_graph(self, g=None, directed=False):
        if self._pkg == "networkx":
            import networkx as nx
            from sgcn.graph import NetworkxGraph
            
            if not g:
                if directed:
                    g = nx.DiGraph()
                else:
                    g = nx.Graph()            
                    
            return NetworkxGraph(g)
        elif self._pkg == "igraph":
            import igraph         
            from sgcn.graph import IgraphGraph
            
            if not g:
                g = igraph.Graph(directed=directed)
            return IgraphGraph(g)

        else:
            raise RuntimeError("[SYSTEM] should not be reached here...")
                               
                                           
                               
from aoc.utils.common import read_lines

class Reactor:
    def __init__(self, test=False):
        self.test = test
        self.lines=read_lines(test)
        self.rows=len(self.lines)
        self.graph=dict()
        self.visited=dict()
        self.start = "you"
        self.end = "out"



    def populate_directed_graph(self):
        for line in self.lines:
            colon_idx = line.find(':')
            root=line[0:colon_idx].strip()
            elements=[ele.strip() for ele in line[colon_idx+1:].split(" ") if ele.strip()!='']
            if root not in self.graph:
                self.graph[root]=elements

    def print_graph(self):
        for i in self.graph.keys():
            print(f"key :{i} val : {self.graph[i]}")
        print(f"len of graph {len(self.graph)}")
    
    def count_paths(self,node):
        if node=="out":
            return 1
        if node in self.visited:
            return self.visited[node]
        paths=0
        for v in self.graph[node]:
            paths+=self.count_paths(v)
        self.visited[node]=paths
        return self.visited[node]

    def solve(self):
        self.populate_directed_graph()
        #self.print_graph()
        print(f"Total Paths from you to out : {self.count_paths('you')}")

if __name__ == "__main__":
    reactor = Reactor()
    reactor.solve()

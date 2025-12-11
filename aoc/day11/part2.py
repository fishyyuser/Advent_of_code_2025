from aoc.utils.common import read_lines

class Reactor:
    def __init__(self, test=False):
        self.test = test
        self.lines=read_lines(test)
        self.rows=len(self.lines)
        self.graph=dict()
        self.visited={}


    def populate_directed_graph(self):
        for line in self.lines:
            colon_idx = line.find(':')
            root=line[0:colon_idx].strip()
            elements=[ele.strip() for ele in line[colon_idx+1:].split(" ") if ele.strip()!='']
            if root not in self.graph:
                self.graph[root]=elements
    
    def _dfs(self,node,target):
        if node==target:
            return 1
        if node=='out' and target!='out':
            return 0
        if node in self.visited:
            return self.visited[node]
        paths=0
        for v in self.graph[node]:
            paths+=self._dfs(v,target)
        self.visited[node]=paths
        return self.visited[node]
    
    def count_paths(self,start,end):
        self.visited={}
        return self._dfs(start,end)

    def solve(self):
        self.populate_directed_graph()
        a1=self.count_paths('svr','fft')
        a2=self.count_paths('svr','dac')
        b1=self.count_paths('fft','dac')
        b2=self.count_paths('dac','fft')
        c1=self.count_paths('fft','out')
        c2=self.count_paths('dac','out')
        # a1*b1*c2 svr -> fft -> dac -> out
        # a2*b2*c1 svr -> dac -> fft -> out
        print(f"Total Paths from svr to out (with fft + dac) : {(a1*b1*c2+a2*b2*c1)}")

if __name__ == "__main__":
    reactor = Reactor()
    reactor.solve()

from aoc.utils.common import read_lines
class TreeFarm:
    def __init__(self, test=False):
        self.lines = read_lines(test)
        self.shapes = []
        self.dimensions = []
        self.req = []
        self.hash_counts = []

    def populate_shape(self):
        s=[]
        for i in range(31):
            if i%5==0: continue
            if i%5==4:
                self.shapes.append(s)
                s=[]
                continue
            s.append(list(self.lines[i].strip()))

    def rotate_shape(self,m): return [list(r) for r in zip(*m[::-1])]
    def flip_shape(self,m): return [list(r) for r in zip(*m)]
    def trim_shape(self,m):
        f=[(i,j) for i in range(len(m)) for j in range(len(m[0])) if m[i][j]=='#']
        if not f: return [[]]
        a=min(i for i,j in f); b=max(i for i,j in f)
        c=min(j for i,j in f); d=max(j for i,j in f)
        return [row[c:d+1] for row in m[a:b+1]]

    def tuplify(self,m): return tuple(tuple(r) for r in m)

    def shape_transformations(self):
        out=[]; hc=[]
        for s in self.shapes:
            v=set()
            cur=s
            for _ in range(4):
                v.add(self.tuplify(self.trim_shape(cur)))
                v.add(self.tuplify(self.trim_shape(self.flip_shape(cur))))
                cur=self.rotate_shape(cur)
            o=[[list(r) for r in t] for t in v]
            out.append(o)
            hc.append(sum(r.count('#') for r in o[0]))
        self.shapes=out
        self.hash_counts=hc

    def populate_dimensions_and_req(self):
        for line in self.lines[30:]:
            if not line.strip(): continue
            d,r=line.split(":")
            self.dimensions.append(tuple(int(x) for x in d.split("x")))
            self.req.append(tuple(int(x) for x in r.split()))

    def gen_bitboards(self,R,C):
        out=[[] for _ in self.shapes]
        for sid,orients in enumerate(self.shapes):
            for sh in orients:
                h=len(sh); w=len(sh[0])
                for i in range(R-h+1):
                    for j in range(C-w+1):
                        m=0; ok=True
                        for a in range(h):
                            for b in range(w):
                                if sh[a][b]=='#':
                                    gi=i+a; gj=j+b
                                    if gi>=R or gj>=C: ok=False; break
                                    m |= 1<<(gi*C+gj)
                            if not ok: break
                        if ok and m: out[sid].append(m)
        return out

    def can_fill(self,dim,req):
        R,C=dim
        if sum(req[i]*self.hash_counts[i] for i in range(6)) > R*C: return False
        pl=self.gen_bitboards(R,C)
        inst=[]
        for sid,cnt in enumerate(req):
            for _ in range(cnt): inst.append(sid)
        for sid in inst:
            if not pl[sid]: return False
        inst.sort(key=lambda x: len(pl[x]))
        memo=set()
        def backtrack(i,mask):
            if i==len(inst): return True
            k=(i,mask)
            if k in memo: return False
            sid=inst[i]
            for pm in pl[sid]:
                if mask & pm: continue
                if backtrack(i+1,mask|pm): return True
            memo.add(k)
            return False
        return backtrack(0,0)

    def solve(self):
        self.populate_shape()
        self.shape_transformations()
        self.populate_dimensions_and_req()
        regions_filled=0
        for d,r in zip(self.dimensions,self.req):
            if self.can_fill(d,r): regions_filled+=1
        print("\nRegions that can fill the present :", regions_filled)

if __name__=="__main__":
    farm=TreeFarm()
    farm.solve()

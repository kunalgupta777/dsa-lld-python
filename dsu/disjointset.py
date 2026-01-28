import random
"""
Disjoint Set Data Structure. 
We perform two operations here:
1. Find(x) -> tells us the parent of x 
2. Union(x, y) -> merges the sets of x and y
We optimize both Find and Union by using path compression and union by size (or rank, we didn't use it here)

TC: find, union, and belongs all work in O(alpha(n)) where alpha(n) is the inverse ackermann function
For all practical purposes alpha(n) <= 4, so all operations are essentially O(1)
"""
class DisjointSet:
    def __init__(self, n: int) -> None:
        """
        n elements numbered from 0 to n-1
        """
        self.n = n
        self.parent = [i for i in range(self.n)]
        self.size = [1]*self.n
    
    def find(self, e: int) -> int:
        if self.parent[e] != e:
            self.parent[e] = self.find(self.parent[e])
        return self.parent[e]
    
    def union(self, a: int, b: int) -> None:
        ra = self.find(a)
        rb = self.find(b)

        if ra != rb:
            if self.size[ra] > self.size[rb]:
                self.parent[rb] = ra
                self.size[ra] += self.size[rb]

            else:
                self.parent[ra] = rb
                self.size[rb] += self.size[ra]
    
    def belongs(self, a: int, b: int) -> bool:
        """
        Returns True if and and b belong to the same set
        """
        return self.find(a) == self.find(b)

if __name__ == "__main__":
    n = 1000
    pairs = [(random.randint(0, n-1), random.randint(0, n-1)) for _ in range(2*n)]
    dsu = DisjointSet(n=n)
    for a, b in pairs:
        dsu.union(a, b)
    # print(dsu.parent)
    for _ in range(100):
        a, b = random.randint(0, n-1), random.randint(0, n-1)
        if dsu.belongs(a, b):
            print("%d and %d belong to the same set" % (a, b))
        else:
            print("%d and %d do not belong to the same set" % (a, b))





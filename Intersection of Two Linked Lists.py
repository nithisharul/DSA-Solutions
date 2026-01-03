class Solution:
    def getIntersectionNode(self, a, b):
        p, q = a, b
        while p != q:
            p = p.next if p else b
            q = q.next if q else a
        return p

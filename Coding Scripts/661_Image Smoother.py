from itertools import product

class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m,n = len(img), len(img[0])
        A = [[0]*n for i in range(m)]
        for i,j in product(range(m), range(n)):
            s = []
            for I,J in product(range(max(0,i-1), min(i+2,m)), range(max(0,j-1),min(j+2,n))):
                s.append(img[I][J])
            A[i][j] = int(sum(s)/len(s))
        return A

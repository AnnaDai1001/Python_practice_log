class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        # hashMap
        d1 = {x:i for i,x in enumerate(list1)}
        d2 = {x:d1[x]+i for i,x in enumerate(list2) if x in d1}
        res = []
        MIN = float('inf')
        
        for x in d2:
            if d2[x] < MIN:
                res = [x]
                MIN = d2[x]
            elif d2[x] == MIN:
                res.append(x)
        
        return res
        
        # use intersection of sets
        # d = {x: list1.index(x)+list2.index(x) for x in set(list1) & set(list2)}
        # return [x for x in d if d[x]==min(d.values())]

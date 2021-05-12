class Solution:
    def countSegments(self, s: str) -> int:
        return len([i for i in s.split(' ') if i != ""])
        # res = 0
        # segs = s.split(' ')
        # for seg in segs:
        #     if seg:
        #         res += 1
        # return res

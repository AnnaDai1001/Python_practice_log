class Solution:
    def judgeCircle(self, moves: str) -> bool:
        return moves.count('U')==moves.count('D') and moves.count('L')==moves.count('R')
        # dic = {'U': 0,
        #       'D': 0,
        #       'L': 0,
        #       'R': 0}
        # for m in moves:
        #     dic[m] += 1
        # return dic['U']==dic['D'] and dic['L']==dic['R']

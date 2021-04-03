class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        S = S.replace("-","").upper()
        remainder = len(S)%K
        first_grp = [S[0:remainder]]
        other_grps = [S[i:i+K] for i in range(remainder, len(S), K)]
        if remainder: return "-".join(first_grp+other_grps)
        return "-".join(other_grps)

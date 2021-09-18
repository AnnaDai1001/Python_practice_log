class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.replace('-', '')
        head = len(s)%k
        groups = []
        
        if head:
            groups.append(s[:head])
        
        for i in range(head, len(s), k):
            groups.append(s[i:(i+k)])
        
        return '-'.join(groups).upper()

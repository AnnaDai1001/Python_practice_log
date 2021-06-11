class Solution:
    def lengthLongestPath(self, s: str) -> int:
        # use stack
        # each element is a tuple with the current total length, depth
        
        paths, stack, ans = s.split('\n'), [], 0
        
        for path in paths:
            segments = path.split('\t')
            depth = len(segments) - 1
            end = segments[-1] # directory or file
            l = len(end)
            while stack and stack[-1][1] >= depth:
                stack.pop()
            if not stack:
                stack.append((l, depth))
            else:
                stack.append((l+stack[-1][0], depth)) # depth stands for the number of extra '\'
            if '.' in end:
                ans = max(ans, stack[-1][0] + stack[-1][1])
        return ans

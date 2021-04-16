class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(w[::-1] for w in s.split(' '))
        # rev_words = []
        # words = list(s.split(" "))
        # for word in words:
        #     rev_words.append(word[::-1])
        # return " ".join(rev_words)

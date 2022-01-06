        # use set
        res = []
        row1 = set('qwertyuiop')
        row2 = set('asdfghjkl')
        row3 = set('zxcvbnm')
        for word in words:
            letters = set(word.lower())
            if (row1&letters == letters) or (row2&letters == letters) or (row3&letters == letters):
                res.append(word)
        return res
      
      
        # brute-force
        row1 = list('qwertyuiop') # ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p']
        row2 = list('asdfghjkl') #['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'] 
        row3 = list('zxcvbnm') #list('zxcvbnm'.split())
        res = []
        for word in words:
            cnt1 = 0
            cnt2 = 0
            cnt3 = 0
            for l in word:
                if l.lower() in row1: cnt1 += 1
                if l.lower() in row2: cnt2 += 1
                if l.lower() in row3: cnt3 += 1
            if cnt1 == len(word) or cnt2 == len(word) or cnt3 == len(word):
                res.append(word)
        return res

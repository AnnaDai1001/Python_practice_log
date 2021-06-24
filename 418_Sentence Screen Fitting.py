# Given a rows x cols screen and a sentence represented by a list of words, find how many times the given sentence can be fitted on the screen.
# http://bookshadow.com/weblog/2016/10/09/leetcode-sentence-screen-fitting/
# https://github.com/YaokaiYang-assaultmaster/LeetCode/blob/master/LeetcodeAlgorithmQuestions/418.%20Sentence%20Screen%20Fitting.md

# https://www.youtube.com/watch?v=e987rKv1d7E

class Solution:
  def wordsTyping(self, sentence, rows, cols):
    s = ' '.join(sentence) + ' '
    n = len(s)
    total_len = 0 # effective length: contain the chars themselves and the space after each word
    
    for r in range(rows):
      total_len += cols
      if s[total_len%n] == ' ':
        total_len += 1
      else:
        while s[(total_len-1)%n] != ' ' and total_len > 0:
          total_len -= 1
    
    return total_len // n
      
# Time complexity : O(rows*longest length of word)

class Solution:
  def wordsTyping(self, sentence, rows, cols): # how to use brute force
    

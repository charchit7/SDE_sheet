# https://leetcode.com/problems/valid-anagram/description/

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # case 1 : sort the array
        # return sorted(s) == sorted(t)

        # case 2 : hashmaps
        # return Counter(s) == Counter(t)

        #case 3 : actually create hashmaps
        # base case check for the len equality 
        if len(s) != len(t):
            return False
        
        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT


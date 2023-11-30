class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        count = {}
        res = 0

        start = 0
        for idx, val in enumerate(s):
            count[val] = 1 + count.get(val, 0)

            # condition to check if our window size is valid wrt k 
            # len window - count of most freq character <= k
            # increase our result counterr

            if (idx-start+1) - max(count.values()) > k:
                # since we are shifting further we are no longer considering the 
                # value at that idx 
                count[s[start]] -=1  
                start +=1

            res = max(res, idx-start+1)
        
        return res
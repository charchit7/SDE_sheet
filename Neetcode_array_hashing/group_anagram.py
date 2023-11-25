#https://leetcode.com/problems/group-anagrams/description/

# method 1 : using sorting.
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hashmap = {}

        for string in strs:
            # Convert the sorted list to a tuple
            sorted_tuple = tuple(sorted(string))

            if sorted_tuple in hashmap:
                hashmap[sorted_tuple].append(string)
            else:
                hashmap[sorted_tuple] = [string]
                    
        return list(hashmap.values())

# method 2 : optimal counting. 
class Solution2:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        from collections import defaultdict

        hashset = defaultdict(list)

        for string in strs:
            characterset = [0] * 26
            for chars in string:
                characterset[ord(chars) - ord("a")] +=1
            hashset[tuple(characterset)].append(string)

        return hashset.values
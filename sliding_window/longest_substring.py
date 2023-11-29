# https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, A: str) -> int:
        # Dictionary to store the index of the last seen occurrence of each character
        seen = {}
        
        # Pointers to track the start and stop indices of the current substring
        start = 0
        stop = 0

        # Iterate through the string using enumerate to get both index and value
        for index, val in enumerate(A):
            # If the character is not in the seen dictionary, update stop
            if val not in seen:
                stop = max(stop, index - start + 1)
            else:
                # If the character is seen, check if its last occurrence is before the current substring
                if seen[val] < start:
                    stop = max(stop, index - start + 1)
                else:
                    # Update the start pointer to the next index after the last occurrence of the character
                    start = seen[val] + 1
            
            # Update the last seen index of the character in the dictionary
            seen[val] = index
        
        # Return the length of the longest substring without repeating characters
        return stop

r'''
Explanation:

The function lengthOfLongestSubstring uses two pointers (start and stop) and a dictionary (seen) to find the length of the longest substring without repeating characters.

The for loop iterates through the string using enumerate to get both the index and value of each character.

If the character is not in the seen dictionary, it updates the stop pointer to the maximum of its current value and the length of the current substring.

If the character is seen, it checks if its last occurrence is before the current substring. If yes, it updates the stop pointer similarly.

If the character is seen and its last occurrence is within the current substring, it updates the start pointer to the next index after the last occurrence of the character.

 The last seen index of each character is updated in the seen dictionary.

The function returns the length of the longest substring without repeating characters.

Time Complexity: O(n)

The function iterates through the string once with two pointers and performs constant time operations for each character.
Space Complexity: O(min(n, m))

The space used by the seen dictionary is proportional to the size of the character set (m), which is at most the size of the alphabet (26 for lowercase and uppercase letters). Therefore, the space complexity is O(min(n, m)), where n is the length of the input string.
'''



########### GOOD solution
def length_of_longest_substring(s):
    char_index_map = {}
    start = max_length = 0

    for end, char in enumerate(s):
        if char in char_index_map and char_index_map[char] >= start:
            start = char_index_map[char] + 1

        char_index_map[char] = end
        max_length = max(max_length, end - start + 1)

    return max_length

# Example usage:
s = "abcabcbb"
result = length_of_longest_substring(s)
print("Length of Longest Substring Without Repeating Characters:", result)

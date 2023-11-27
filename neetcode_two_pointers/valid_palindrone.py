#  https://leetcode.com/problems/valid-palindrome/description/

s = "A man, a plan, a canal: Panama"

r'''
Explanation:

The isPalindrome function uses two pointers (left_p and right_p) to iterate through the string from both ends towards the center.

The first while loop continues until the two pointers meet in the middle. Inside the loop:

The nested while loops move the pointers toward the center, skipping non-alphanumeric characters.
The if statement checks if the characters at the current positions are equal (case-insensitive). If not, it returns False, indicating that the string is not a palindrome.

After the loop, if no inequality is found, it means the string is a palindrome, and the function returns True.

The isalpha function is a helper function that returns True if a character is alphanumeric, using the ord function to check ASCII values.

Time Complexity: O(N)

The algorithm iterates through the string once with two pointers, making it linear in terms of time complexity.
Space Complexity: O(1)

The algorithm uses only a constant amount of extra space, regardless of the input size.
'''

class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        # Initialize two pointers at the beginning and end of the string
        left_p, right_p = 0, len(s) - 1 

        # Continue the loop until the two pointers meet in the middle
        while left_p < right_p:

            # Move the left pointer to the right until it points to an alphanumeric character
            while left_p < right_p and not self.isalpha(s[left_p]):
                left_p += 1

            # Move the right pointer to the left until it points to an alphanumeric character
            while left_p < right_p and not self.isalpha(s[right_p]):
                right_p -= 1
            
            # Check if the characters at the left and right pointers are equal (case-insensitive)
            if s[left_p].lower() != s[right_p].lower():
                return False

            # Move the pointers inward
            left_p += 1 
            right_p -= 1
        
        # If the loop completes without returning False, the string is a palindrome
        return True

    
    def isalpha(self, c):
        # Helper function to check if a character is alphanumeric
        return (ord('A') <= ord(c) <= ord('Z') or 
                ord('a') <= ord(c) <= ord('z') or
                ord("0") <= ord(c) <= ord('9'))


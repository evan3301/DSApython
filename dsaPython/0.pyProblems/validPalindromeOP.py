'''
class Solution:
    def isPalindrome(self, s:str) -> bool:
        newStr = ''

        for c in s:
            if c.isalnum():
                newStr += c.lower()
        return newStr = newStr[::-1]
'''

'''
Proposed solution:

    Two ptr:
        Left ptr
        Right ptr

        Start at ends:
            Decrement pointers for every match
                if meet in middle:
                    return True

        Check for alphanumerical + whitespaces via ascii codes
'''

class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        while left < right:
            # If not isAlphaNum, skip char and pass pointer along
            while left < right and not self.isAlphaNum(s[left]):
                left += 1
            while right < left and not self.isAlphaNum(s[right]):
                right -= 1

            if s[left].lower != s[right].lower:
                return False

            left, right = left + 1, right - 1

        return True

    # Helper function to handle edge cases
    def isAlphaNum(self, c):
        # If char c is between ascii codes between 'A' and 'Z'
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))
# TODO: inputted a string, return True if it is a valid palindrome, False if not
# Palindrome consideration occurs after removal of all non-alphanumeric characters

'''
Proposed solution:
    varA = input str
    varB = varA.reverse()

    compare each char in varA and varB
        if same:
            return True
        else:
            return False
'''

'''
Edge cases:
    string s is empty
    capitalization is different forward and backwards
    whitespace is different forward and backwards
    special char eg. grammar & punctualization
'''

class Solution:
    def isPalindrome(self, s: str) -> bool:
        rev = s[::-1]

        for i in range(len(s)):
            if s[i] != rev[i]:
                return False
        return True
# TODO: given characters (), {}, [], return true if correct pairings in correct order

'''
Proposed solution:
    make list = ['()', '{}', '[]']
        check two input elements to see if in list
            if not return False
            else return True
'''

class Solution:
    def isValid(self, s: str) -> bool:
        self.valid = ['()','{}','[]',]
        s = {}
        for i in range(len(s)):
            if [i, i+1] in self.valid:
                return True
            else:
                return False

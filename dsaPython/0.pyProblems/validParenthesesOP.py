'''
Proposed solution:
    match every closing char to its corresponding opening char
        hashmap

stack implement
Time complexity: O(n)
'''

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close_to_open = {')':'(', '}':'{', ']':'[',}

        for i in s:
            if i in close_to_open:
                # Basecase: stack is not empty & element in top of stack(stack[-1]) is matching open char
                if stack and stack[-1] == close_to_open[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
 
        # Return true if stack is empty
        return True if not stack else False
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for char in s:
            # Current char is digit and alpha
            if char != ']':
                stack.append(char)
            # Current char is ']', means we need to pop the stack and do the multiplication
            else:
                string = ''
                # Pop the stack until we find '[', get the string
                while stack and stack[-1] != '[':
                    string = stack.pop() + string
                # Pop '['
                stack.pop()
                k = ''
                # Pop the stack until we find a digit
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k
                stack.append(string * int(k))
        return ''.join(stack)

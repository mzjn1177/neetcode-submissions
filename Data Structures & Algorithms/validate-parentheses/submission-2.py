class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        corresponding = {")":"(", "]":"[","}":"{"}

        for x in s:
            if x in corresponding:
                if stack and stack[-1] == corresponding[x]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(x)
        return True if not stack else False
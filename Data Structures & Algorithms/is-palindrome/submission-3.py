class Solution:
    def isPalindrome(self, s: str) -> bool:
        S = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        print(S)
        left = 0
        right = len(S) - 1

        while(left < right):
            if S[left] == S[right]:
                left += 1
                right -= 1
            else:
                return False
        return True
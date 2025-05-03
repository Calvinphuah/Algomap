class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # Goal: check if s is a subsequence of t
        # Intuition: Use pointers (2 of them one for s one for t)

        S, T = len(s), len(t)
        if s == "": return True
        if S > T: return False

        i, j = 0, 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            # j increases no matter sucess or fail
            j += 1

        # Once it finishes we check
        return i == len(s)

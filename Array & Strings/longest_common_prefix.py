class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Goal: find the longest common prefix
        # Intuition: First find the shortest length
        # Then keep checking until we find a diff character

        min_length = float('inf')

        # Now we got the shortest length so we know the max we can iterate
        for s in strs:
            if len(s) < min_length:
                min_length = len(s)

        i = 0
        while i < min_length:
            # Compare each string with the first string
            for s in strs:
                if s[i] != strs[0][i]:
                    return s[:i]

            i += 1

        # If it all passes
        return strs[0][:i]

        # Time: O(n * m) where n is the number of strings, m is the min word length
        # Space: O(1)

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # Goal: Merge the string alternately
        # Intuition: use array, while one is not empty yet keep adding if one is empty just add the rest
        # Have an if check if one is empty or not
        # Use the length

        len1, len2 = len(word1), len(word2)
        i, j = 0, 0
        res = []

        while i < len1 or j < len2:
            if i < len1:
                res.append(word1[i])
                i += 1

            if j < len2:
                res.append(word2[j])
                j += 1

        return ''.join(res)

        # Time: O(N) cause loop through
        # Space: O(N)

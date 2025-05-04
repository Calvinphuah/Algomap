class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        # Goal create ranges
        # Intuition: Use pointer

        res = []
        i = 0

        while i < len(nums):
            start = nums[i]
            # Keep going until we dont exceed
            # Get the whole length
            while i < len(nums) - 1 and nums[i] + 1 == nums[i + 1]:
                i += 1

            # Create the string to add
            if start != nums[i]:
                res.append(str(start) + '->' + str(nums[i]))
            else: # It is the same number only one
                res.append(str(start))

            # Once we added move on to the next iteration
            i += 1

        return res



class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        # Goal: Return the number closest to 0 using abs too
        # Intuition: use abs and keep the closest
        closest = nums[0]

        for n in nums:
            if abs(n) < abs(closest):
                closest = n

        # Create a check to see if there is a positive number
        if closest < 0 and abs(closest) in nums:
            return abs(closest)
        else:
            return closest

    # Time: O(n) because we are loop through the whole input
    # Space: O(1)

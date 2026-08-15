class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
          """
          Input: List of integers
          Process: Search if the difference exists in the HashMap as a key
          Output: List containing the indices of the two numbers that add to the target
          """

          nums_dict = dict()

          for i in range(len(nums)):
            difference = target - nums[i]

            if difference in nums_dict: # Check if the difference is an existing key in the dictionary
                return [nums_dict[difference], i]

            nums_dict[nums[i]] = i # key = num, value = index
            
class Solution(object):

    def two_sum(self, nums, val):
        if nums is None or val is None:
            raise TypeError("nums or val cannot be None")
        if len(nums) == 0:
            raise ValueError("nums cannot be empty")
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == val:
                    return [i, j]
        return None

if __name__ == "__main__":
    obj = Solution()
    print(obj.two_sum([1, 2, 3, 4, 5, 6], 12))
    print(obj.two_sum([1, 2, 3, 4, 5, 6], None))

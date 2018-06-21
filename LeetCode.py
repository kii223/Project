class Solution:
    def twoSum(self, nums, target):
        mapList = {}
        for i in range(0,len(nums)):
            mapList[nums[i]] = i
        print(mapList)
        for j in range(0, len(nums)):
            try:
                return [j, mapList[(target - nums[j])]]
            except:
                continue

test = Solution()
print(test.twoSum([3,2,4],6))



class Solution:
    def twoSum(nums, target):
        hashmap = {}
        numLength = len(nums)
        for i in range(numLength):
            print("putting %i into hash index %i" %(nums[i], i))
            hashmap[nums[i]] = i
        for i in range(numLength):
            complement = target - nums[i]
            if complement in hashmap and hashmap[complement] != i:
                return [i, hashmap[complement]]

if __name__ == '__main__':
    sol = Solution.twoSum([2,7,11,15], 9)
    print(sol)
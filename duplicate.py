class Solution:
    def __init__(self, nums) -> None:
        self.nums = nums
    def getNums(self):
        return self.nums
    
    def containsDuplicate(self) -> bool:
        nums = self.getNums()
        hashmap = {}

        for i in range(len(nums)):
            if nums[i] in hashmap:
                return True
            hashmap[i] = nums[i]
        return False


        # for i in range(len(nums)):
        #     hashmap[nums[i]] = i
        # return len(hashmap) != len(nums)


        # c = 2
        # for i in nums:
        #     for j in nums[c:]:
        #         if i == j:
        #             return True
        #     c+=1
        # return False

if __name__ == '__main__':
    e1 = Solution([1,2,3,1])
    print('e1: ' , e1.containsDuplicate())
    e2 = Solution([1,2,3,4])
    print('e2: ' , e2.containsDuplicate())
    e3 = Solution([1,1,1,3,3,4,3,2,4,2])
    print('e3: ' , e1.containsDuplicate())

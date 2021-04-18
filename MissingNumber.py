from typing import List

def missingNumber(nums: List[int]) -> int:
    missing = len(nums)
    # temp = range(0, len(nums))
    # print(temp)
    for i in range(0, len(nums)): # checks to see what is missing from the list
        # print(i)
        if i not in nums:
            missing = i


    return missing


nums = [3,0,1]
print(missingNumber(nums)) # returns 2
test = [0,1]
test2 = [9,6,4,2,3,5,7,0,1]
test3 = [0]
print(missingNumber(test)) # returns 2
print(missingNumber(test2)) # returns 8
print(missingNumber(test3)) # returns 1
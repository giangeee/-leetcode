# coding=utf-8
# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def twoSum(nums, target):
    two = []
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if (nums[i] + nums[j] == target):
                two.append(i)
                two.append(j)
                return two


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    nums = [2,7,11,15]
    target = 9
    print twoSum(nums, target)
    nums2 = [3,2,3]
    target2 = 6
    print twoSum(nums2,target2)
    nums3 = [2,5,5,11]
    target3 = 10
    print twoSum(nums3, target3)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/

from typing import List

def distributeCandies(candyType: List[int]) -> int:
    # types = []
    # [types.append(i) for i in candyType if i not in types] # checks to see if there are any duplicates
    # # print(types)
    #
    # if len(types) == 1:
    #     return 1
    # else:
    #     if len(types)%2 == 0:
    #         return int(len(candyType)/2)
    #     else:
    #         return 3
    # print(candyType)
    # test = set(candyType).union()
    # return test
    return min(len(set(candyType)), len(candyType)//2) # // ignores the remainder


# test = [1,1,2,2,3,3] # returns 3
# test2 = [1,1,2,3] # returns 2
# test3 = [6,6,6,6] # returns 1
test4 = [1,1,1,1,2,2,2,3,3,3] # returns 3

# print(distributeCandies(test))
# print(distributeCandies(test2))
# print(distributeCandies(test3))
print(distributeCandies(test4))

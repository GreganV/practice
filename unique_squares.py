def unique_squares(list_nums):
    squares = [ ]
    for i in range(0,4):
        squares.append((list_nums[i])**2)
   
    print(squares)
unique_squares([2,3,2,9])

def unique_squares_but_bad(nums):

    return[num*num for num in set(nums)]




def unique_squares_but_good(nums):
    squared = []
    for num in nums:
        if num*num not in squared:
            squared.append(num*num)
    return squared

print(unique_squares_but_good(2,3,2,9))

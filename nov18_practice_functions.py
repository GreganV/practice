import random as r
def make_random_list(num,range_start,range_end):
    num_list = []
    for i in range(0,num):

        num_list.insert(i,r.randint(range_start,range_end))

    return num_list

print (make_random_list(20, 1,400))

def ask_for_list():
    num = int(input("enter how many digits you want: "))
    range_start = int(input("enter the the minimum: "))
    range_end = int(input("enter the maximum: "))

    return(make_random_list(num,range_start,range_end))

print(ask_for_list())


number1 = float(input("Enter 1 Number: "))
number2 = float(input("Enter Another Number:"))
if number1 > number2:
    print(number1)
if number1 < number2:
    print(number2)


def find_max(a,b):
    if a > b:
        return a
    return b 

find_max(18,90)

def return_top_two(a,b,c,):
    temp = [a,b,c]
    return temp[1], temp[2]
best, next_best = return_top_two(95,78,2)

top = return_top_two(3245,56,1333525464)

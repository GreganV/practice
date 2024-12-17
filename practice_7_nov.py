
def check_within_ten(num):
    
    num = int(num)
    if 90 <= num <= 110:
        return True
    else:
        return False

print(check_within_ten(73))
print(check_within_ten(95))
print(check_within_ten(103))
print(check_within_ten(117))
        

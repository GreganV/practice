def string_explosion(str):
    str_list = " "
    for i in range(len(str)):
        str_list +=str[:i+1]
    return(str_list)

print(string_explosion("hello"))

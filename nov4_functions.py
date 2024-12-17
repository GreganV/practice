def in1020(a,b):
    if a >= 10 and a <= 20:
        return True
    elif b>= 10 and b<= 20:
        return True
    else:
        return False

print(in1020(15,20))

def not_string(str):
    if "not" in str:
        print(str)
    else:
        print("not "+str)

not_string("happy")

#dictionaries!

alien = {"home planet" :"Mars",
      "skin color" :"green",
      "age":90,
      "number of eyes" :90,
      "fingers" :"10 on each hand",
      "languages spoken":["spanish", "klingon", "dutch"]}
print(alien["languages spoken"])
      
# alien.keys()
alien.keys()
alien.values()
alien.items()

for key in alien.keys():
    print(alien[key])

for item in alien.items():
    print(item)

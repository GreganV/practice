rooms = {"room1":{"S": "room2"},
        "room2": {"E": "room3", "N": "room1"},
        "room3": {"W":"room2","S": "room4","E":"room5"},
        "room4": {"N":"room3"},
        "room5": {"W":"room3","N":"room6"},
        "room6": {"S":"room5"}}
def choose_direction(room):
    print("you are in a room. there are doors in the following directions:")
    print(rooms[room.keys()])
    choice= input("Which direction: ")
    return"room1"

choose_direction("room1")

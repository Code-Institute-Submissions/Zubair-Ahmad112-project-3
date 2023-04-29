import random

size_limit = [5, 15]


ships = [
    {
        "name": "Aircraft Carrier",
        "size": 5,
        "symbol": "A"
    },
    {
        "name": "Battleship",
        "size": 4,
        "symbol": "B"
    },
    {
        "name": "Submarine",
        "size": 3,
        "symbol": "S"
    },
    {
        "name": "Destroyer",
        "size": 3,
        "symbol": "D"
    },
    {
        "name": "Patrol Boat",
        "size": 2,
        "symbol": "P"
    }
]

hit_symbol = "X"
miss_symbol = "M"

battlefield = []
pc_battlefield = []

while True:
    size = int(input("Enter the size of the battlefield (#x#): "))
    if size < size_limit[0]:
        print(f"Please enter a positive integer greater than {size_limit[0] - 1}.")
        continue    
    if size > size_limit[1]:
        print(f"Please enter a positive integer less than {size_limit[1]}.")
        continue
    break

for i in range(size):
    battlefield.append([])
    for j in range(size):
        battlefield[i].append("O")

    pc_battlefield.append([])
    for j in range(size):
        pc_battlefield[i].append("O")

def print_battlefield():
    print("=====YOUR BATTLEFIELD=====")
    print("  ", end="")
    for i in range(size):
        print(chr(i + 65), end=" ")
    print()
    for i in range(size):
        print(chr(i + 65), end=" ")
        for j in range(size):
            print(battlefield[i][j], end=" ")
        print()

def print_pc_battlefield(show_ships=False):
    print("=====PC BATTLEFIELD=====")
    print("  ", end="")
    for i in range(size):
        print(chr(i + 65), end=" ")
    print()
    for i in range(size):
        print(chr(i + 65), end=" ")
        for j in range(size):
            if not show_ships:
                c = pc_battlefield[i][j]
                if c == "A" or c == "B" or c == "S" or c == "D" or c == "P":
                    print("O", end=" ")
                    continue
            print(pc_battlefield[i][j], end=" ")
        print()

print_battlefield()

# Place ships
for ship in ships:
    print(f"Placing {ship['name']}...")
    while True:
        direction = input("Enter the direction (H/V): ")
        if direction.upper() != "H" and direction.upper() != "V":
            print("Please enter H or V.")
            continue
   
        x = input("Enter the x coordinate: ")

        x = x.upper()
        x = ord(x)
        x = x - 65
        if x < 0 or x > size - 1:
            print(f"Please enter a letter between A and {chr(size + 64)}.")
            continue
   
        y = input("Enter the y coordinate: ")

        y = y.upper()
        y = ord(y)
        y = y - 65
        if y < 0 or y > size - 1:
            print(f"Please enter a letter between A and {chr(size + 64)}.")
            continue
   
        if direction.upper() == "H":
            if x + ship["size"] > size:
                print(f"Please enter a letter between A and {chr(size + 65 - ship['size'])}.")
                continue
            retry = False
            for i in range(ship["size"]):
                if battlefield[y][x + i] != "O":
                    print("There is already a ship there.")
                    retry = True
                    break
            if retry:
                continue
            for i in range(ship["size"]):
                battlefield[y][x + i] = ship["symbol"]
        else:
            if y + ship["size"] > size:
                print(f"Please enter a letter between A and {chr(size + 65 - ship['size'])}.")
                continue
            retry = False
            for i in range(ship["size"]):
                if battlefield[y + i][x] != "O":
                    print("There is already a ship there.")
                    retry = True
                    break
            if retry:
                continue
            for i in range(ship["size"]):
                battlefield[y + i][x] = ship["symbol"]
        print_battlefield()
        break

# Place PC ships
for ship in ships:
    while True:
        direction = random.randint(0, 1)
        if direction == 0:
            direction = "H"
        else:
            direction = "V"
        y = random.randint(0, size - 1)
        x = random.randint(0, size - 1)
        if direction.upper() == "H":
            if y + ship["size"] > size:
                continue
            retry = False
            for i in range(ship["size"]):
                if pc_battlefield[x][y + i] != "O":
                    retry = True
                    break
            if retry:
                continue
            for i in range(ship["size"]):
                pc_battlefield[x][y + i] = ship["symbol"]
        else:
            if x + ship["size"] > size:
                continue
            retry = False
            for i in range(ship["size"]):
                if pc_battlefield[x + i][y] != "O":
                    retry = True
                    break
            if retry:
                continue
            for i in range(ship["size"]):
                pc_battlefield[x + i][y] = ship["symbol"]
        break

print_battlefield()
print_pc_battlefield(True)

print("=====BATTLE START=====")
print()
print("A = Aircraft Carrier")
print("B = Battleship")
print("S = Submarine")
print("D = Destroyer")
print("P = Patrol Boat")
print("O = Empty")
print("X = Hit")
print("M = Miss")
print()

pc_ships_sunk = []
ships_sunk = []

for ship in ships:
    pc_ships_sunk.append(0)
    ships_sunk.append(0)

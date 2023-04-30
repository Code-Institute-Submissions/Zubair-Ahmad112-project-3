import random

size_limit = [5, 15]
ships = [{
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
empty_symbol = "O"

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
        battlefield[i].append(empty_symbol)

    pc_battlefield.append([])
    for j in range(size):
        pc_battlefield[i].append(empty_symbol)

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
                skip = False
                for ship in ships:
                    if c == ship["symbol"]:
                        print(empty_symbol, end=" ")
                        skip = True
                        break
                if skip:
                    continue
            print(pc_battlefield[i][j], end=" ")
        print()

print_battlefield()

for ship in ships:
    print(f"Placing {ship['name']}...")
    while True:
        direction = input("Enter the direction (H/V): ")
        if direction.upper() != "H" and direction.upper() != "V":
            print("Please enter H or V.")
            continue
   
        y = input("Enter the x coordinate: ")
        # Coordinates start FROM ASKII CODE 65
        y = y.upper()
        y = ord(y)
        y = y - 65
        if y < 0 or y > size - 1:
            print(f"Please enter a letter between A and {chr(size + 64)}.")
            continue
   
        x = input("Enter the y coordinate: ")

        x = x.upper()
        x = ord(x)
        x = x - 65
        if x < 0 or x > size - 1:
            print(f"Please enter a letter between A and {chr(size + 64)}.")
            continue
   
        if direction.upper() == "H":
            if y + ship["size"] > size:
                print(f"Please enter a letter between A and {chr(size + 65 - ship['size'])}.")
                continue
            retry = False
            for i in range(ship["size"]):
                if battlefield[x][y + i] != empty_symbol:
                    print("There is already a ship there.")
                    retry = True
                    break
            if retry:
                continue
            for i in range(ship["size"]):
                battlefield[x][y + i] = ship["symbol"]
        else:
            if x + ship["size"] > size:
                print(f"Please enter a letter between A and {chr(size + 65 - ship['size'])}.")
                continue
            retry = False
            for i in range(ship["size"]):
                if battlefield[x + i][y] != empty_symbol:
                    print("There is already a ship there.")
                    retry = True
                    break
            if retry:
                continue
            for i in range(ship["size"]):
                battlefield[x + i][y] = ship["symbol"]
        print_battlefield()
        break
    
# Place PC ships randomly
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
                if pc_battlefield[x][y + i] != empty_symbol:
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
                if pc_battlefield[x + i][y] != empty_symbol:
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
for ship in ships:
    print(f"{ship['symbol']} = {ship['name']} | size: {ship['size']}")

print(f"{empty_symbol} = Empty")
print(f"{hit_symbol} = Hit")
print(f"{miss_symbol} = Miss")
print()

pc_ships_sunk = []
ships_sunk = []

for ship in ships:
    pc_ships_sunk.append(0)
    ships_sunk.append(0)

while True:        
    print("=====YOUR TURN=====")
    while True:
        y = input("Enter the x coordinate: ")
        y = y.upper()
        y = ord(y)
        y = y - 65
        if y < 0 or y > size - 1:
            print(f"Please enter a letter between A and {chr(size + 64)}.")
            continue
   
        x = input("Enter the y coordinate: ")

        x = x.upper()
        x = ord(x)
        x = x - 65
        if x < 0 or x > size - 1:
            print(f"Please enter a letter between A and {chr(size + 64)}.")
            continue
        break

    if pc_battlefield[x][y] == hit_symbol or pc_battlefield[x][y] == miss_symbol:
        print("You already shot there.")
        continue

    if pc_battlefield[x][y] == "O":
        print("Miss!")
        pc_battlefield[x][y] = miss_symbol

    else:
        print("Hit!")
        ship_hit = pc_battlefield[x][y]
        pc_battlefield[x][y] = hit_symbol
        for i in range(len(ships)):
            if ships[i]["symbol"] == ship_hit:
                ships_sunk[i] += 1
                if ships_sunk[i] == ships[i]["size"]:
                    print(f"You sunk the {ships[i]['name']}!")
                    print()
                    
                    # Check if all ships are sunk
                    all_sunk = True
                    for j in range(len(ships)):
                        if ships_sunk[j] != ships[j]["size"]:
                            all_sunk = False
                            break
                    if all_sunk:
                        print_battlefield()
                        print_pc_battlefield(True)
                        print("=====YOU WIN=====")
                        exit()
                break
    print_pc_battlefield()
    print("=====PC TURN=====")
    while True:
        x = random.randint(0, size - 1)
        y = random.randint(0, size - 1)
        if battlefield[x][y] == hit_symbol or battlefield[x][y] == miss_symbol:
            continue

        if battlefield[x][y] == "O":
            print(f"PC missed at {chr(x + 65)}{chr(y + 65)}!")
            battlefield[x][y] = miss_symbol
        else:
            print(f"PC hit at {chr(x + 65)}{chr(y + 65)}!")
            ship_hit = battlefield[x][y]
            battlefield[x][y] = hit_symbol
            for i in range(len(ships)):
                if ships[i]["symbol"] == ship_hit:
                    pc_ships_sunk[i] += 1
                    if pc_ships_sunk[i] == ships[i]["size"]:
                        print(f"PC sunk the {ships[i]['name']}!")
                        print()
                        
                        # Check if all ships are sunk
                        all_sunk = True
                        for j in range(len(ships)):
                            if pc_ships_sunk[j] != ships[j]["size"]:
                                all_sunk = False
                                break

                        if all_sunk:
                            print_battlefield()
                            print_pc_battlefield(True)
                            print("=====PC WINS=====")
                            exit()
                    break
        break
        
        

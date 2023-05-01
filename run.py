""" 
    This is the main file for the Battleship game.
"""

import random
import sys

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

HIT_SYMBOL = "X"
MISS_SYMBOL = "M"
EMPTY_SYMBOL = "O"

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
        battlefield[i].append(EMPTY_SYMBOL)

    pc_battlefield.append([])
    for j in range(size):
        pc_battlefield[i].append(EMPTY_SYMBOL)

# Prints the battlefield.
def print_battlefield():
    """Prints the battlefield."""
    print("=====YOUR BATTLEFIELD=====")
    print("  ", end="")
    for k in range(size):
        print(chr(k + 65), end=" ")
    print()
    for k in range(size):
        print(chr(k + 65), end=" ")
        for l in range(size):
            print(battlefield[k][l], end=" ")
        print()

def print_pc_battlefield(show_ships=False):
    """
    Prints the PC battlefield.
    Keyword arguments:
    show_ships -- if True, shows the ships on the battlefield (default False)
    """
    print("=====PC BATTLEFIELD=====")
    print("  ", end="")
    for k in range(size):
        print(chr(k + 65), end=" ")
    print()
    for k in range(size):
        print(chr(k + 65), end=" ")
        for l in range(size):
            if not show_ships:
                current_char = pc_battlefield[k][l]
                skip = False
                for ship in ships:
                    if current_char == ship["symbol"]:
                        print(EMPTY_SYMBOL, end=" ")
                        skip = True
                        break
                if skip:
                    continue
            print(pc_battlefield[k][l], end=" ")
        print()

print_battlefield()

for ship in ships:
    print(f"Placing {ship['name']}...")
    while True:
        DIRECTION = input("Enter the direction (H/V): ")
        if DIRECTION.upper() != "H" and DIRECTION.upper() != "V":
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

        if DIRECTION.upper() == "H":
            if y + ship["size"] > size:
                print(f"Please enter a letter between A and {chr(size + 65 - ship['size'])}.")
                continue
            RETRY = False
            for i in range(ship["size"]):
                if battlefield[x][y + i] != EMPTY_SYMBOL:
                    print("There is already a ship there.")
                    RETRY = True
                    break
            if RETRY:
                continue
            for i in range(ship["size"]):
                battlefield[x][y + i] = ship["symbol"]
        else:
            if x + ship["size"] > size:
                print(f"Please enter a letter between A and {chr(size + 65 - ship['size'])}.")
                continue
            RETRY = False
            for i in range(ship["size"]):
                if battlefield[x + i][y] != EMPTY_SYMBOL:
                    print("There is already a ship there.")
                    RETRY = True
                    break
            if RETRY:
                continue
            for i in range(ship["size"]):
                battlefield[x + i][y] = ship["symbol"]
        print_battlefield()
        break

# Place PC ships randomly
for ship in ships:
    while True:
        DIRECTION = random.randint(0, 1)
        if DIRECTION == 0:
            DIRECTION = "H"
        else:
            DIRECTION = "V"
        y = random.randint(0, size - 1)
        x = random.randint(0, size - 1)
        if DIRECTION.upper() == "H":
            if y + ship["size"] > size:
                continue
            RETRY = False
            for i in range(ship["size"]):
                if pc_battlefield[x][y + i] != EMPTY_SYMBOL:
                    RETRY = True
                    break
            if RETRY:
                continue
            for i in range(ship["size"]):
                pc_battlefield[x][y + i] = ship["symbol"]
        else:
            if x + ship["size"] > size:
                continue
            RETRY = False
            for i in range(ship["size"]):
                if pc_battlefield[x + i][y] != EMPTY_SYMBOL:
                    RETRY = True
                    break
            if RETRY:
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

print(f"{EMPTY_SYMBOL} = Empty")
print(f"{HIT_SYMBOL} = Hit")
print(f"{MISS_SYMBOL} = Miss")
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

    if pc_battlefield[x][y] == HIT_SYMBOL or pc_battlefield[x][y] == MISS_SYMBOL:
        print("You already shot there.")
        continue

    if pc_battlefield[x][y] == "O":
        print("Miss!")
        pc_battlefield[x][y] = MISS_SYMBOL

    else:
        print("Hit!")
        ship_hit = pc_battlefield[x][y]
        pc_battlefield[x][y] = HIT_SYMBOL
        for i, ship in enumerate(ships):
            if ship["symbol"] == ship_hit:
                ships_sunk[i] += 1
                if ships_sunk[i] == ship["size"]:
                    print(f"You sunk the {ship['name']}!")
                    print()

                    # Check if all ships are sunk
                    ALL_SUNK = True
                    for j,ship2 in enumerate(ships):
                        if ships_sunk[j] != ship2["size"]:
                            ALL_SUNK = False
                            break
                    if ALL_SUNK:
                        print_battlefield()
                        print_pc_battlefield(True)
                        print("=====YOU WIN=====")
                        sys.exit(0)
                break
    print_pc_battlefield()
    print("=====PC TURN=====")
    while True:
        x = random.randint(0, size - 1)
        y = random.randint(0, size - 1)
        if battlefield[x][y] == HIT_SYMBOL or battlefield[x][y] == MISS_SYMBOL:
            continue

        if battlefield[x][y] == "O":
            print(f"PC missed at {chr(x + 65)}{chr(y + 65)}!")
            battlefield[x][y] = MISS_SYMBOL
        else:
            print(f"PC hit at {chr(x + 65)}{chr(y + 65)}!")
            ship_hit = battlefield[x][y]
            battlefield[x][y] = HIT_SYMBOL
            for i, ship in enumerate(ships):
                if ship["symbol"] == ship_hit:
                    pc_ships_sunk[i] += 1
                    if pc_ships_sunk[i] == ship["size"]:
                        print(f"PC sunk the {ship['name']}!")
                        print()

                        # Check if all ships are sunk
                        ALL_SUNK = True
                        for j, ship2 in enumerate(ships):
                            if pc_ships_sunk[j] != ship2["size"]:
                                ALL_SUNK = False
                                break

                        if ALL_SUNK:
                            print_battlefield()
                            print_pc_battlefield(True)
                            print("=====PC WINS=====")
                            sys.exit(0)
                    break
        break

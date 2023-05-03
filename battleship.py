import random


class Battleship:
    def __init__(self):
        self.size_limit = [5, 15]
        self.ships = [
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
        self.hit_symbol = "X"
        self.miss_symbol = "M"
        self.empty_symbol = "O"
        self.battlefield = []
        self.pc_battlefield = []
        self.pc_ships_sunk = []
        self.ships_sunk = []

    def get_size(self):
        while True:
            try:
                self.size = int(
                    input("Enter the size of the battlefield (#x#): "))
                if self.size < self.size_limit[0]:
                    print(
                        f"Please enter a number greater than {self.size_limit[0] - 1}.")
                    continue
                if self.size > self.size_limit[1]:
                    print(
                        f"Please enter a number less than {self.size_limit[1]}.")
                    continue
                break
            except ValueError:
                print("Please enter a valid number.")

    def create_battlefield(self):
        for i in range(self.size):
            self.battlefield.append([])
            for j in range(self.size):
                self.battlefield[i].append(self.empty_symbol)

            self.pc_battlefield.append([])
            for j in range(self.size):
                self.pc_battlefield[i].append(self.empty_symbol)

    def print_battlefield(self):
        print("=====YOUR BATTLEFIELD=====")
        print("  ", end="")
        for i in range(self.size):
            print(chr(i + 65), end=" ")
        print()
        for i in range(self.size):
            print(chr(i + 65), end=" ")
            for j in range(self.size):
                print(self.battlefield[i][j], end=" ")
            print()

    def print_pc_battlefield(self, show_ships=False):
        print("=====PC BATTLEFIELD=====")
        print("  ", end="")
        for i in range(self.size):
            print(chr(i + 65), end=" ")
        print()
        for i in range(self.size):
            print(chr(i + 65), end=" ")
            for j in range(self.size):
                if not show_ships:
                    c = self.pc_battlefield[i][j]
                    skip = False
                    for ship in self.ships:
                        if c == ship["symbol"]:
                            print(self.empty_symbol, end=" ")
                            skip = True
                            break
                    if skip:
                        continue
                print(self.pc_battlefield[i][j], end=" ")
            print()

    def place_ships(self):
        for ship in self.ships:
            self.ships_sunk.append(0)
            print(f"Placing {ship['name']}...")
            while True:
                try:
                    direction = input("Enter the direction (H/V): ")
                    if direction.upper() != "H" and direction.upper() != "V":
                        print("Please enter H or V.")
                        continue

                    y = input("Enter the x coordinate: ")
                    # Coordinates start FROM ASKII CODE 65
                    y = y.upper()
                    y = ord(y)
                    y = y - 65
                    if y < 0 or y > self.size - 1:
                        print(
                            f"Please enter a letter between A and {chr(self.size + 64)}.")
                        continue

                    x = input("Enter the y coordinate: ")

                    x = x.upper()
                    x = ord(x)
                    x = x - 65
                    if x < 0 or x > self.size - 1:
                        print(
                            f"Please enter a letter between A and {chr(self.size + 64)}.")
                        continue

                    if direction.upper() == "H":
                        if y + ship["size"] > self.size:
                            print(
                                f"Please enter a letter between A and {chr(self.size + 64 - ship['size'])}.")
                            continue
                        retry = False
                        for i in range(ship["size"]):
                            if self.battlefield[x][y + i] != self.empty_symbol:
                                print("There is already a ship there.")
                                retry = True
                                break
                        if retry:
                            continue
                        for i in range(ship["size"]):
                            self.battlefield[x][y + i] = ship["symbol"]
                    else:
                        if x + ship["size"] > self.size:
                            print(
                                f"Please enter a letter between A and {chr(self.size + 64 - ship['size'])}.")
                            continue
                        retry = False
                        for i in range(ship["size"]):
                            if self.battlefield[x + i][y] != self.empty_symbol:
                                print("There is already a ship there.")
                                retry = True
                                break
                        if retry:
                            continue
                        for i in range(ship["size"]):
                            self.battlefield[x + i][y] = ship["symbol"]
                    self.print_battlefield()
                    break
                except e:
                    print("Please enter a valid character.")

    def place_pc_ships(self):
        for ship in self.ships:
            self.pc_ships_sunk.append(0)
            while True:
                direction = random.randint(0, 1)
                if direction == 0:
                    direction = "H"
                else:
                    direction = "V"
                y = random.randint(0, self.size - 1)
                x = random.randint(0, self.size - 1)
                if direction.upper() == "H":
                    if y + ship["size"] > self.size:
                        continue
                    retry = False
                    for i in range(ship["size"]):
                        if self.pc_battlefield[x][y + i] != self.empty_symbol:
                            retry = True
                            break
                    if retry:
                        continue
                    for i in range(ship["size"]):
                        self.pc_battlefield[x][y + i] = ship["symbol"]
                else:
                    if x + ship["size"] > self.size:
                        continue
                    retry = False
                    for i in range(ship["size"]):
                        if self.pc_battlefield[x + i][y] != self.empty_symbol:
                            retry = True
                            break
                    if retry:
                        continue
                    for i in range(ship["size"]):
                        self.pc_battlefield[x + i][y] = ship["symbol"]
                break

    def check_if_sunk(self, x, y, pc=False):
        if pc:
            battlefield = self.pc_battlefield
            sunk = self.ships_sunk
        else:
            battlefield = self.battlefield
            sunk = self.pc_ships_sunk
        for i, ship in enumerate(self.ships):
            if battlefield[x][y] == ship["symbol"]:
                sunk[i] += 1
                if sunk[i] == ship["size"]:
                    return True
        return False

    def user_turn(self):
        print("=====YOUR TURN=====")
        while True:
            try:
                y = input("Enter the x coordinate: ")
                y = y.upper()
                y = ord(y)
                y = y - 65
                if y < 0 or y > self.size - 1:
                    print(
                        f"Please enter a letter between A and {chr(self.size + 64)}.")
                    continue

                x = input("Enter the y coordinate: ")
                x = x.upper()
                x = ord(x)
                x = x - 65
                if x < 0 or x > self.size - 1:
                    print(
                        f"Please enter a letter between A and {chr(self.size + 64)}.")
                    continue

                if self.pc_battlefield[x][y] == self.empty_symbol:
                    self.pc_battlefield[x][y] = self.miss_symbol
                    print("You missed.")
                    break
                elif self.pc_battlefield[x][y] == self.hit_symbol:
                    print("You already hit there.")
                    continue
                else:
                    print("You hit a ship.")
                    if self.check_if_sunk(x, y, pc=True):
                        print("You sunk a ship.")
                    self.pc_battlefield[x][y] = self.hit_symbol
                    break
            except e:
                print("Please enter a valid character.")

    def pc_turn(self):
        print("=====PC TURN=====")
        while True:
            x = random.randint(0, self.size - 1)
            y = random.randint(0, self.size - 1)
            if self.battlefield[x][y] == self.empty_symbol:
                self.battlefield[x][y] = self.miss_symbol
                print("PC missed.")
                break
            elif self.battlefield[x][y] == self.hit_symbol:
                print("PC already hit there.")
                continue
            else:
                print("PC hit a ship.")
                if self.check_if_sunk(x, y):
                    print("PC sunk a ship.")
                self.battlefield[x][y] = self.hit_symbol
                break

    def check_if_game_over(self, pc=False):
        if pc:
            sunk = self.pc_ships_sunk
        else:
            sunk = self.ships_sunk
        for i, ship in enumerate(self.ships):
            if sunk[i] != ship["size"]:
                return False
        return True

    def start(self):
        self.get_size()
        self.create_battlefield()
        self.print_battlefield()
        self.place_ships()
        self.place_pc_ships()
        self.print_battlefield()
        self.print_pc_battlefield(True)
        while True:
            self.user_turn()
            if self.check_if_game_over():
                print("You won.")
                break
            self.pc_turn()
            if self.check_if_game_over(True):
                print("PC won.")
                break
        self.print_battlefield()
        self.print_pc_battlefield(True)
        print("Game over.")


game = Battleship()
game.start()

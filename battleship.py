import random

size_limit = [5, 15]

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

def print_pc_battlefield():
    print("=====PC BATTLEFIELD=====")
    print("  ", end="")
    for i in range(size):
        print(chr(i + 65), end=" ")
    print()
    for i in range(size):
        print(chr(i + 65), end=" ")
        for j in range(size):
            print(pc_battlefield[i][j], end=" ")
        print()

print_pc_battlefield()
print_battlefield()

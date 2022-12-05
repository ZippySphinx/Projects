"""
Problem Statement
The Tower of Hanoi is a puzzle where we have three rods and n disks. The three rods are:

1. source
2. destination
3. auxiliary

Initally, all the n disks are present on the source rod. The final objective of the puzzle is to move all disks from the source rod to the destination rod using the auxiliary rod. However, there are some rules according to which this has to be done:

1. Only one disk can be moved at a time.
2. A disk can be moved only if it is on the top of a rod.
3. No disk can be placed on the top of a smaller disk.

You will be given the number of disks num_disks as the input parameter.

For example, if you have num_disks = 3, then the disks should be moved as follows:

    1. move disk from source to auxiliary
    2. move disk from source to destination
    3. move disk from auxiliary to destination

You must print these steps as follows:

    S A
    S D
    A D

Where S = source, D = destination, A = auxiliary
"""

def tower_of_hanoi(num_disks, source, auxillary, destination):
    if num_disks == 0:
        return
    if num_disks == 1:
        print("{} {}".format(source, destination))
        return
    tower_of_hanoi(num_disks - 1, source, destination, auxillary)
    print("{} {}".format(source, destination))
    tower_of_hanoi(num_disks - 1, auxillary, source, destination)

print("Tower of Hanoi for 1")
tower_of_hanoi(1, "S", "A", "D")
print("Tower of Hanoi for 2")
tower_of_hanoi(2, "S", "A", "D")
print("Tower of Hanoi for 3")
tower_of_hanoi(3, "S", "A", "D")
print("Tower of Hanoi for 4")
tower_of_hanoi(4, "S", "A", "D")
print("Tower of Hanoi for 5")
tower_of_hanoi(5, "S", "A", "D")

# Advent of Code
# Day 3
# https://adventofcode.com/2025/day/3


file = open("./Day_03/input.txt", "r")
input = file.readlines()

batteries = []
for inp in input:
    batteries.append(inp[0:-1])

sum = 0
for bank in batteries:
    highest_number = 0
    for i in range(0, len(bank) - 1):
        for j in range(i+1, len(bank)):
            number = int(bank[i]) * 10 + int(bank[j])
            if number > highest_number:
                highest_number = number
    print(highest_number)
    sum += highest_number
print("First Puzzle:", sum)



print("Second Puzzle:")

# Advent of Code
# Day 2
# https://adventofcode.com/2025/day/2


file = open("./Day_02/input.txt", "r")
input = file.readlines()[0]
input = input.split(",")

ranges = []
for string in input:
    values = string.split("-")
    ranges.append([int(values[0]), int(values[1])])

sum_invalid_ids = 0

for ran in ranges:
    for i in range(ran[0], ran[1]+1):
        i = str(i)
        if len(i) % 2 == 0:  # is the number of digits even
            half = int(len(i) / 2)
            if i[0:half] == i[half:]:
                sum_invalid_ids += int(i)
print("First Puzzle:", sum_invalid_ids)



print("Second Puzzle:")

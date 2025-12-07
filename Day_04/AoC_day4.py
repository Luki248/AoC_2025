# Advent of Code
# Day 4
# https://adventofcode.com/2025/day/4


file = open("./Day_04/input.txt", "r")
input = file.readlines()

wall = []
for line in input:
    wall.append(line[:-1])

i_max = len(wall) - 1
j_max = len(wall[0]) - 1

total_rolls_to_pick = 0
for i in range(i_max + 1):
    for j in range(j_max + 1):
        if wall[i][j] != "@":
            continue
        neihbours = 0
        if i > 0 and j > 0:
            if wall[i-1][j-1] == "@" or wall[i-1][j-1] == "x":
                neihbours += 1
        if i > 0:
            if wall[i-1][j] == "@" or wall[i-1][j] == "x":
                neihbours += 1
        if i > 0 and j < j_max:
            if wall[i-1][j+1] == "@" or wall[i-1][j+1] == "x":
                neihbours += 1
        if j > 0:
            if wall[i][j-1] == "@" or wall[i][j-1] == "x":
                neihbours += 1
        if j < j_max:
            if wall[i][j+1] == "@" or wall[i][j+1] == "x":
                neihbours += 1
        if j > 0 and i < i_max:
            if wall[i+1][j-1] == "@" or wall[i+1][j-1] == "x":
                neihbours += 1
        if i < i_max:
            if wall[i+1][j] == "@" or wall[i+1][j] == "x":
                neihbours += 1
        if i < i_max and j < j_max:
            if wall[i+1][j+1] == "@" or wall[i+1][j+1] == "x":
                neihbours += 1
        if neihbours < 4:
            total_rolls_to_pick += 1
            wall[i] = wall[i][:j] + "x" + wall[i][j+1:]
print("First Puzzle:", total_rolls_to_pick)


print("Second Puzzle:")

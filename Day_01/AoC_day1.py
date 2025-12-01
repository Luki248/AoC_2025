# Advent of Code
# Day 1
# https://adventofcode.com/2025/day/1


file = open("./Day_01/input.txt", "r")
input = file.readlines()

number_of_0 = 0
dial_position = 50

for code in input:
    direction = code[0]
    amount = int(code[1:-1])
    
    if direction == "R":
        dial_position += amount
        while dial_position > 99:
            dial_position -= 100
    else:
        dial_position -= amount
        while dial_position < 0:
            dial_position += 100
    #print(direction, amount, dial_position)

    if dial_position == 0:
        number_of_0 += 1

print("First Puzzle:", number_of_0)


number_of_0 = 0
dial_position = 50
old_position = 50

for code in input:
    direction = code[0]
    amount = int(code[1:-1])
    
    old_position = dial_position

    if direction == "R":
        dial_position += amount
        if dial_position == 0:
            if old_position != 0:
                number_of_0 += 1
        else:
            while dial_position > 99:
                dial_position -= 100
                number_of_0 += 1
    else:
        dial_position -= amount
        if dial_position == 0:
            if old_position != 0:
                number_of_0 += 1
        else:
            while dial_position < 0:
                dial_position += 100
                number_of_0 += 1

    print(direction, amount, dial_position, number_of_0)

print("Second Puzzle:", number_of_0)

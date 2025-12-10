# Advent of Code
# Day 5
# https://adventofcode.com/2025/day/5


file = open("./Day_05/input.txt", "r")
input = file.readlines()

ranges = []
ingredients = []

do_ranges = True
for line in input:
    if line == "\n":
        do_ranges = False
    elif do_ranges:
        start_range = int(line.split("-")[0])
        stop_range = int(line.split("-")[1])
        ranges.append([start_range, stop_range])
    else:
        ingredients.append(int(line[:-1]))


total_of_fresh = 0
for ingr in ingredients:
    is_fresh = False
    for rang in ranges:
        if ingr >= rang[0] and ingr <= rang[1]:
            is_fresh = True
    if is_fresh:
        total_of_fresh += 1

print("First Puzzle:", total_of_fresh)


all_ranges = [3]
for rang in ranges:
    if min(all_ranges) > rang[1]:
        temp = range(rang[0], rang[1] + 1)
        all_ranges.extend(temp)
    elif max(all_ranges) < rang[0]:
        temp = range(rang[0], rang[1] + 1)
        all_ranges.extend(temp)
    else:
        for i in range(rang[0], rang[1] + 1):
            if all_ranges.count(i) < 1:
                all_ranges.append(i)
print("Second Puzzle:", len(all_ranges))

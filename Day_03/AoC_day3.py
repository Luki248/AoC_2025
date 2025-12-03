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
        for j in range(i + 1, len(bank)):
            number = int(bank[i]) * 10 + int(bank[j])
            if number > highest_number:
                highest_number = number
    #print(highest_number)
    sum += highest_number
print("First Puzzle:", sum)


sum = 0
index = 0
for bank in batteries:
    highest_number = 0
    for i01 in range(0, len(bank) - 11):
        for i02 in range(i01 + 1, len(bank) - 10):
            for i03 in range(i02 + 1, len(bank) - 9):
                for i04 in range(i03 + 1, len(bank) - 8):
                    for i05 in range(i04 + 1, len(bank) - 7):
                        for i06 in range(i05 + 1, len(bank) - 6):
                            for i07 in range(i06 + 1, len(bank) - 5):
                                for i08 in range(i07 + 1, len(bank) - 4):
                                    for i09 in range(i08 + 1, len(bank) - 3):
                                        for i10 in range(i09 + 1, len(bank) - 2):
                                            for i11 in range(i10 + 1, len(bank) - 1):
                                                for i12 in range(i11 + 1, len(bank)):
                                                    number =  int(bank[i01]) * 100000000000 \
                                                            + int(bank[i02]) * 10000000000 \
                                                            + int(bank[i03]) * 1000000000 \
                                                            + int(bank[i04]) * 100000000 \
                                                            + int(bank[i05]) * 10000000 \
                                                            + int(bank[i06]) * 1000000 \
                                                            + int(bank[i07]) * 100000 \
                                                            + int(bank[i08]) * 10000 \
                                                            + int(bank[i09]) * 1000 \
                                                            + int(bank[i10]) * 100 \
                                                            + int(bank[i11]) * 10 \
                                                            + int(bank[i12])
                                                    if number > highest_number:
                                                        highest_number = number
    index += 1
    print(f"{index:3}/200 {highest_number}")
    sum += highest_number
print("Second Puzzle:", sum)

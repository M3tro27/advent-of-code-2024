with open("input.txt") as f:
    lines = f.readlines()
lines = 'a'.join(lines)

print(lines)
print("""
###################
#     PART ONE    #
###################
""")

import re

matches = re.findall("mul\\(\\d+,\\d+\\)", lines)

def multiplying(lst):
    mult_sum = 0
    for match in lst:
        cal = re.findall("\\d+", match)
        # print(cal)
        mult_sum += int(cal[0]) * int(cal[1])
    return mult_sum

print("Multiplication: ", multiplying(matches))

print("""
###################
#     PART TWO    #
###################
""")

dos = []
print(f"Lines: {lines}\n")
lst = lines.split("don't()")
print(f"Splitted by dont: {lst}\n")
dos.append(lst[0])
lst.pop(0)
print(f"Popped list: {lst}\n")
print(f"Dos: {dos}\n")

for string in lst:
    print(f"String v listu: {string}\n")
    if string.find("do()") >= 1:
        x = string.split("do()")
        print(f"List splited by do: {x}\n")
        x.pop(0)
        dos += x

print(f"Dos po joinu: {dos}\n")
print(dos[0])

matches = re.findall("mul\\(\\d+,\\d+\\)", ''.join(dos))

print("Multiplication: ", multiplying(matches))
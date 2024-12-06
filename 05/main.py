with open("input.txt") as f:
    lines = [line.strip() for line in f.readlines()]

# print(lines)

rules = lines[:lines.index("")]
lines = lines[lines.index("") + 1:]

# print(rules)
# print(lines)

##### Transforming list of strings to nested list of ints
lines = [list(map(int, line.split(','))) for line in lines]
print(lines)

##### Transforming list of strings to dict
new_rules = []
for rule in rules:
    new_rules.append([int(rule.split('|')[0]), int(rule.split('|')[1])])
print(new_rules)

def sum_of_middle(lst):
    return sum([line[len(line) // 2] for line in lst])

print("""
###################
#     PART ONE    #
###################
""")

def pairs_of_number(number):
    return [y for x, y in new_rules if x == number]

def is_valid(lst):
    valid = True
    for i, number in enumerate(line):
        for pair in pairs_of_number(number):
            if pair in line:
                pair_index = line.index(pair)
                if pair_index < i:
                    valid = False
                    break
        if not valid:
            break
    return valid

correct = []
uncorrect = []
# for line in lines:
#     x = []
#     for number in line:
#         if number in new_rules:
#             if new_rules[number] in line:
#                 if line.index(number) < line.index(new_rules.get(number)):
#                     x.append(number)
#                     continue
#                 else:
#                     x = []
#                     break
#             else:
#                 x.append(number)
#                 continue
#     if x:
#         correct.append(x)

for line in lines:
    if is_valid(line):
        correct.append(line)
    else:
        uncorrect.append(line)

print(f"Correct lines: {correct}")
print(f"Uncorrect lines: {uncorrect}")


print(f"Sum of correct lines: {sum_of_middle(correct)}")

print("""
###################
#     PART TWO    #
###################
""")

corrected = []
for line in uncorrect:
    while not is_valid(line):
        for i, number in enumerate(line):
            for pair in pairs_of_number(number):
                if pair in line:
                    pair_index = line.index(pair)
                    if pair_index < i:
                        line[pair_index], line[i] = line[i], line[pair_index]
    corrected.append(line)

print(f"Corrected lines: {corrected}")
print(f"Sum of corrected line: {sum_of_middle(corrected)}")




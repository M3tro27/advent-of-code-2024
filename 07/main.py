from helpers import file_open

lines = file_open("input.txt", ": ")
# print(lines)

equations = []
for line in lines:
    equations.append([int(line[0]), [int(number) for number in line[1].split(" ")]])
print(equations)

print("""
###################
#     PART ONE    #
###################
""")

def find_combinations(numbers, base, current_value=None):
    if current_value is None:
        current_value = numbers[0]
        numbers = numbers[1:]

    if current_value == base and not numbers:
        return True

    if not numbers:
        return False

    first, rest = numbers[0], numbers[1:]

    if find_combinations(rest, base, current_value + first):
        return True

    elif find_combinations(rest, base, current_value * first):
        return True

    return False

result = 0
for key, value in equations:
    if find_combinations(value, key):
        print(f"Match found: {key}, {value}")
        result += key

print(f"Sum: {result}")


print("""
###################
#     PART TWO    #
###################
""")

def find_combinations_2(numbers, base, current_value=None):
    if current_value is None:
        current_value = numbers[0]
        numbers = numbers[1:]

    if current_value == base and not numbers:
        return True

    if not numbers:
        return False

    first, rest = numbers[0], numbers[1:]

    if find_combinations_2(rest, base, current_value + first):
        return True

    elif find_combinations_2(rest, base, current_value * first):
        return True

    elif find_combinations_2(rest, base, int(str(current_value) + str(first))):
        return True

    return False

result = 0
for key, value in equations:
    if find_combinations_2(value, key):
        print(f"Match found: {key}, {value}")
        result += key

print(f"Sum: {result}")
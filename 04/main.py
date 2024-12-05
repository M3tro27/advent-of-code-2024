with open("input.txt") as f:
    lines = [line.strip() for line in f.readlines()]

print(lines)

print("""
###################
#     PART ONE    #
###################
""")

def horizontal(lst):
    count = 0
    for string in lst:
        # print(string)
        if "XMAS" in string:
            # print(f"Horizontal: {string}")
            count += string.count("XMAS")
        if "SAMX" in string:
            # print(f"Horizontal reverse: {string}")
            count += string.count("SAMX")
    return count

def vertical(lst):
    x = []
    for i in range(len(lst[0])):
        column = ''
        for string in lst:
            column += string[i]
        x.append(column)
    return horizontal(x)

def diagonal(lst):
    n = len(lst)
    all_diagonals = []

    for start in range(-n + 1, n):
        diagonal_lr = ''.join(lst[i][i - start] for i in range(max(0, start), min(n, n + start)))
        all_diagonals.append(diagonal_lr)

    for start in range(2 * n - 1):
        diagonal_rl = ''.join(
            lst[i][start - i]
            for i in range(max(0, start - n + 1), min(n, start + 1))
            if 0 <= start - i < len(lst[0])
        )
        all_diagonals.append(diagonal_rl)

    return horizontal(all_diagonals)

print("Horizontal XMAS: ",horizontal(lines))
print("Vertical XMAS: ",vertical(lines))
print("Diagonal XMAS: ",diagonal(lines))

print("Sum: ", horizontal(lines) + vertical(lines) + diagonal(lines))

print("""
###################
#     PART TWO    #
###################
""")

count = 0

for i in range(len(lines)):
    if lines[i] == lines[0] or lines[i] == lines[-1]:
        continue
    indexes = []
    for j, c in enumerate(lines[i]):
        if c == "A":
            indexes.append(j)
    for index in indexes:
        if index == 0 or index == len(lines[i]) - 1:
            continue
        if (
                lines[i - 1][index - 1] + lines[i + 1][index + 1] in ["MS", "SM"]
            and lines[i + 1][index - 1] + lines[i - 1][index + 1] in ["MS", "SM"]
        ):
            print("Condition met")
            count += 1

print(f"Sum of X-MAS: {count}")

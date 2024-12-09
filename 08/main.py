from itertools import combinations

with open("input.txt") as f:
    lines = [line.strip() for line in f.readlines()]

print("""
###################
#     PART ONE    #
###################
""")

def get_chars(lst):
    # Extract unique antenna characters
    return list(set(char for line in lst for char in line if char != "."))


def get_coordinates_of_char(char, lst):
    # Get all coordinates of a specific character
    return [[i, j] for i, line in enumerate(lst) for j, c in enumerate(line) if c == char]


def calculate_nodes(pairs, max_x, max_y):
    # Calculate antinodes for all pairs of coordinates
    nodes = set()  # Use a set to store unique nodes
    for pair in pairs:
        x1, y1 = pair[0]
        x2, y2 = pair[1]

        # Calculate midpoints for antinodes
        dx, dy = x2 - x1, y2 - y1
        node1 = [x1 - dx, y1 - dy]  # Antinode on one side
        node2 = [x2 + dx, y2 + dy]  # Antinode on the other side

        # Check boundaries and add valid nodes
        if 0 <= node1[0] < max_y and 0 <= node1[1] < max_x:
            nodes.add(tuple(node1))  # Add as a tuple to the set
        if 0 <= node2[0] < max_y and 0 <= node2[1] < max_x:
            nodes.add(tuple(node2))
    return nodes


# Extract unique characters (antennas)
chars = get_chars(lines)

# Dimensions of the map
max_y, max_x = len(lines), len(lines[0])

# Process each character
unique_nodes = set()
for char in chars:
    # Get coordinates of all antennas of this frequency
    coordinates = get_coordinates_of_char(char, lines)

    # Generate all pairs of coordinates
    pairs = list(combinations(coordinates, 2))
    # print(pairs)

    # Calculate antinodes and add to the set
    char_nodes = calculate_nodes(pairs, max_x, max_y)
    unique_nodes.update(char_nodes)

# Count total unique nodes (antinodes)
print("Part ONE: ", len(unique_nodes))



print("""
###################
#     PART TWO    #
###################
""")

def recursion_by_subtraction(node, dx, dy, max_x, max_y):
    nodes = set()
    x1, y1 = node
    while 0 <= x1 < max_y and 0 <= y1 < max_x:
        nodes.add((x1, y1))
        x1 -= dx
        y1 -= dy
    return nodes

def recursion_by_addition(node, dx, dy, max_x, max_y):
    nodes = set()
    x1, y1 = node
    while 0 <= x1 < max_y and 0 <= y1 < max_x:
        nodes.add((x1, y1))
        x1 += dx
        y1 += dy
    return nodes

def calculate_nodes_part_two(pairs, max_x, max_y):
    nodes = set()
    for pair in pairs:
        x1, y1 = pair[0]
        x2, y2 = pair[1]

        dx, dy = x2 - x1, y2 - y1

        nodes.add((x1, y1))
        nodes.add((x2, y2))

        nodes.update(recursion_by_subtraction((x1, y1), dx, dy, max_x, max_y))
        nodes.update(recursion_by_addition((x2, y2), dx, dy, max_x, max_y))

    return nodes

unique_nodes = set()

for char in chars:
    coordinates = get_coordinates_of_char(char, lines)
    pairs = list(combinations(coordinates, 2))

    char_nodes = calculate_nodes_part_two(pairs, max_x, max_y)
    unique_nodes.update(char_nodes)

print("Part TWO: ", len(unique_nodes))
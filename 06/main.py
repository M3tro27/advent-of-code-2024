with open("input.txt") as f:
    lines = [line.strip() for line in f.readlines()]

# print(lines)
backup_lines = lines.copy()

def print_picture(lst):
    for line in lst:
        print(line)
    print("\n")

print("""
###################
#     PART ONE    #
###################
""")

from helpers import replace_char_in_string


class Guard:

    def __init__(self, x_coordinate, y_coordinate, direction):
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.direction = direction

    def change_direction(self):
        if self.direction != 3:
            self.direction += 1
        else:
            self.direction = 0

    def __repr__(self):
        return f"X cord: {self.x_coordinate}\nY cord: {self.y_coordinate}\nDirection: {self.direction}"

    def coordinates(self):
        return [self.x_coordinate, self.y_coordinate, self.direction]

    def move_up(self, lst):
        # print_picture(lst)
        while self.y_coordinate > 0 and lst[self.y_coordinate - 1][self.x_coordinate] != "#":
            # if lst[self.y_coordinate - 1][self.x_coordinate] == ".":
            lst[self.y_coordinate] = replace_char_in_string(lst[self.y_coordinate], self.x_coordinate, "X")
            self.y_coordinate -= 1
            lst[self.y_coordinate] = replace_char_in_string(lst[self.y_coordinate], self.x_coordinate, "^")
            # print_picture(lst)
            # print("\n")
        self.change_direction()

    def move_right(self, lst):
        # print_picture(lst)
        while self.x_coordinate < len(lst[0]) - 1 and lst[self.y_coordinate][self.x_coordinate + 1] != "#":
            # if lst[self.y_coordinate][self.x_coordinate + 1] != "X":
            lst[self.y_coordinate] = replace_char_in_string(lst[self.y_coordinate], self.x_coordinate, "X")
            self.x_coordinate += 1
            lst[self.y_coordinate] = replace_char_in_string(lst[self.y_coordinate], self.x_coordinate, ">")
            # print_picture(lst)
            # print("\n")
        self.change_direction()

    def move_down(self, lst):
        # print_picture(lst)
        while self.y_coordinate < len(lst) - 1 and lst[self.y_coordinate + 1][self.x_coordinate] != "#":
            lst[self.y_coordinate] = replace_char_in_string(lst[self.y_coordinate], self.x_coordinate, "X")
            self.y_coordinate += 1
            lst[self.y_coordinate] = replace_char_in_string(lst[self.y_coordinate], self.x_coordinate, "v")
            # print_picture(lst)
            # print("\n")
        self.change_direction()

    def move_left(self, lst):
        # print_picture(lst)
        while self.x_coordinate > 0 and lst[self.y_coordinate][self.x_coordinate - 1] != "#":
            lst[self.y_coordinate] = replace_char_in_string(lst[self.y_coordinate], self.x_coordinate, "X")
            self.x_coordinate -= 1
            lst[self.y_coordinate] = replace_char_in_string(lst[self.y_coordinate], self.x_coordinate, "<")
            # print_picture(lst)
            # print("\n")
        self.change_direction()

repetition_count = 0

is_looped = False
def start_movement(lst):
    stored_coordinates = set()
    while True:
        stored_coordinates.add(tuple(guard.coordinates()))

        if guard.direction == 0:
            guard.move_up(lst)
        elif guard.direction == 1:
            guard.move_right(lst)
        elif guard.direction == 2:
            guard.move_down(lst)
        elif guard.direction == 3:
            guard.move_left(lst)

        if tuple(guard.coordinates()) in stored_coordinates:
            # print("getting looped, aborting...")
            global is_looped
            is_looped = True
            break

        if guard.y_coordinate == len(lst) - 1 or guard.y_coordinate == 0 or \
                guard.x_coordinate == len(lst[0]) - 1 or guard.x_coordinate == 0:
            is_looped = False
            break

    lst[guard.y_coordinate] = replace_char_in_string(lst[guard.y_coordinate], guard.x_coordinate, "X")

for y, line in enumerate(lines):
    for x, char in enumerate(line):
        if char == "^":
            guard = Guard(x, y, 0)
            mem_coordinates = [guard.x_coordinate, guard.y_coordinate, guard.direction]


start_movement(lines)
count = sum(line.count("X") for line in lines)
print(f"Count of areas: {count}")


print("""
###################
#     PART TWO    #
###################
""")

#### Optimisation crying
loops = 0
for y, line in enumerate(lines):
    for x, char in enumerate(line):
        if char == "X":
            new_lines = lines.copy()
            new_lines[y] = replace_char_in_string(new_lines[y], x, "#")
            guard = Guard(mem_coordinates[0], mem_coordinates[1], mem_coordinates[2])
            start_movement(new_lines)
            if is_looped:
                loops += 1

print(f"Total valid loops: {loops}")

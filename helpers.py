def file_open(file_name = "input.txt", split_char = " "):
    with open(file_name) as f:
        return [line.strip().split(split_char) for line in f.readlines()]

"""
Returns a string with replaced character on certain index.
"""
def replace_char_in_string(string, index, char):
    return string[:index] + char + string[index + 1:]

def print_picture(lst):
    for line in lst:
        print(line)
    print("\n")
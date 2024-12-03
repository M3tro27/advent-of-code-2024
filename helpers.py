def file_open(file_name = "input.txt", split_char = " "):
    with open(file_name) as f:
        return [line.strip().split(split_char) for line in f.readlines()]
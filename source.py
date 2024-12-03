def file_load(file_name):
    with open(file_name) as f:
        return [line.strip().split('   ') for line in f.readlines()]
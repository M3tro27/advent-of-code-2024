from helpers import file_open

lines = file_open("input.txt", "   ")

print("""
###################
#     PART ONE    #
###################
""")

data = list(zip(sorted(int(l) for l,_ in lines), sorted(int(r) for _,r in lines)))

difference_sum = sum(abs(l-r) for l, r in data)

print(f"Difference sum: {difference_sum}\n")

print("""
###################
#     PART TWO    #
###################
""")

from collections import Counter

left, right = zip(*((int(l), int(r)) for l, r in lines))

right_count = Counter(right)

similarity_score = sum(l * right_count[l] for l in left)

print(f"Similarity score: {similarity_score}")

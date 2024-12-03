from helpers import file_open

lines = file_open("input.txt", " ")

print("""
###################
#     PART ONE    #
###################
""")

safe_count = 0
unsafe_count = 0

for report in lines:
    if any(a == b for a, b in zip(report, report[1:])):
        unsafe_count += 1
        # print(f"Unsafe 1: {report}\n")

    elif any(abs(int(a) - int(b)) > 3 for a, b in zip(report, report[1:])):
        unsafe_count += 1
        # print(f"Unsafe 2: {report}\n")

    elif not (all(int(a) < int(b) for a, b in zip(report, report[1:])) or all(int(a) > int(b) for a, b in zip(report, report[1:]))):
        unsafe_count += 1
        # print(f"Unsafe 3: {report}\n")

    else:
        safe_count += 1
        # print(f"Safe: {report}\n")

print(f"""Safe reports: {safe_count}\nUnsafe reports: {unsafe_count}""")

print("""
###################
#     PART TWO    #
###################
""")

def is_safe(list):
    if any(a == b for a, b in zip(list, list[1:])):
        return False

    elif any(abs(int(a) - int(b)) > 3 for a, b in zip(list, list[1:])):
        return False

    elif not (all(int(a) < int(b) for a, b in zip(list, list[1:])) or all(int(a) > int(b) for a, b in zip(list, list[1:]))):
        return False

    else:
        return True

safe_count = 0
unsafe_count = 0

for report in lines:
    if is_safe(report):
        safe_count += 1

    else:
        for i in range(len(report)):
            report_copy = report.copy()
            report_copy.pop(i)

            if is_safe(report_copy):
                safe_count += 1
                break


print(f"""Safe reports: {safe_count}\nUnsafe reports: {unsafe_count}""")
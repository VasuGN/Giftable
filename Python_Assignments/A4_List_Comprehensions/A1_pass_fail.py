marks_input = input("Enter marks separated by spaces: ")

marks_list = marks_input.split()

result = []

for mark in marks_list:
    mark = float(mark)

    if mark >= 40:
        result.append("Pass")
    else:
        result.append("Fail")

print(result)
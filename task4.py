# Minimal positive integer: Find minimal positive integer that is not in list.
# Example: [1,2,3,4,6] - Answer 5
# Example: [1,2,3] - Answer 4
# Example: [-1, -2, -6] - Answer 1
# Create effective algorithm

def min_int(ar):
    ar.sort()
    for i in ar:
        if i > 0 and i < ar[-1]:
            i = ar[-1] - 1
        elif i < 0 and i >= ar[-1]:
            i = ar[-1] + 1
            if i == 0:
                i+=1
    return i

print(min_int([-1, -2, -6]))
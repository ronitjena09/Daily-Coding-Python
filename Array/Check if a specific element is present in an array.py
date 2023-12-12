arr = []

num = int(input())  # for array size
c = int(input())  # for specific element

for i in range(num):
    element = int(input())  # for array elements
    arr.append(element)

    if c == element:  # check if present
        print(f"{c} is available in {i+1}th position")

print(arr)

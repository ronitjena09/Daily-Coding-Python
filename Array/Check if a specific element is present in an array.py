arr = []

num = int(input())  # for array size
c = int(input())  # for specific element

for i in range(num):
    element = int(input())  # for array elements
    arr.append(element)

if element in arr:
    print(f"{element} is present in array")

num = int(input())

arr = []

for i in range(num):
    element = int(input())
    arr.append(element)

print(arr[::-1])  # reverses an array

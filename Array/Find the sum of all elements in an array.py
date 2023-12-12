num = int(input())  # taking array size
arr = []

for i in range(num):
    element = int(input(i))  # taking array numbers
    arr.append(element)

print(arr)
print(sum(arr))

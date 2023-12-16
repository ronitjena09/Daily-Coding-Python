num = int(input())
arr = []

index = int(input())
ele = int(input())

for i in range(num):
    element = int(input())
    arr.append(element)
    if index == arr[element]:
        print([ele] + arr) 
    else:
        print(arr)
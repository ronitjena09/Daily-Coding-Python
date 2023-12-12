def rem_dup(arr, num):
    while element in arr:
        arr.remove(element)


num = int(input())
arr = []

for i in range(num):
    element = int(input())
    arr.append(element)

specific_element = int(input())
rem_dup(arr, specific_element)
print(arr)

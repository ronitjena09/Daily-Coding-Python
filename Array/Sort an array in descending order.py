def sort_desc(arr):
    sorted_desc = sorted(arr)
    return sorted_desc


num = int(input())
arr = []
for i in range(num):
    element = int(input())
    arr.append(element)

sorted_desc = sort_desc(arr)
print(sorted_desc[::-1])

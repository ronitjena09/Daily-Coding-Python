def sort_asc(arr):
    sorted_asc = sorted(arr)
    return sorted_asc


num = int(input())
arr = []
for i in range(num):
    element = int(input())
    arr.append(element)

sorted_asc = sort_asc(arr)
print(sorted_asc)

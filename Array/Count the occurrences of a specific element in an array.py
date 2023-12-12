def count_occurence(arr, num):
    count = 0
    for element in arr:
        if element == num:
            count += 1

    return count


num = int(input())
arr = []
for i in range(num):
    element = int(input())
    arr.append(element)

value = int(input())
occurence = count_occurence(arr, value)

print(arr)
print(occurence)

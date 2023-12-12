num = int(input())  # taking input

arr = []  # creating an array

for i in range(num):
    element = int(input())  # taking user input
    arr.append(element)

print(max(arr))  # printing max value

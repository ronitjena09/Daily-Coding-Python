num = int(input())  # TAKES THE INPUT

arr = []  # creating an array

for i in range(num):
    element = int(input())  # taking user input
    arr.append(element)

avg = sum(arr)/num  # calculating average
print(arr)
print(avg)  # printing values

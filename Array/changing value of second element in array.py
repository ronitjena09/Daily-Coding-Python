arr = []
num = int(input())

for i in range (num):
    arr.append(i)
    
if i >= 3:
    c=int(input())
    arr[1]=c
    
print(arr)
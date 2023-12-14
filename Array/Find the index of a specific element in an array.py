def indexEle(arr, element):
    try:  # if element present in array
        return arr.index(element)  # return the element index
    except:
        return -1


num = int(input())  # size of array
arr = []  # creating array


for _ in range(num):  # defining elements in array
    arr.append(int(input()))

ele = int(input())  # for specific element

index = indexEle(arr, ele)

print(index+1)  # printing index of a specific element

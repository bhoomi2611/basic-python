#Sort an array using insertion sort
def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j] :
                arr[j+1] = arr[j]
                j -= 1
        arr[j+1] = key
array=[]
n=int(input("Enter length of array"))
for i in range(0,n):
    m=int(input())
    array.append(m)
insertionSort(array)
print ("Sorted array is:")
for i in range(len(array)):
    print (array[i])
def binarySearch(arr,element):
    s=0
    e=len(arr)-1
    while(s<=e):
        mid=(s+e)//2
        if arr[mid]==element:
            return mid
        elif arr[mid]<element:
            s=mid+1
        else:
            e=mid-1

arr=[1,3,4,6,8,9,12,15,19]
index=binarySearch(arr,8)
print(index)
def ElementsRemoval(arr):
    arr.sort(reverse=True)
    cost=0
    for i in range(len(arr)):
        cost+=arr[i]*(i+1)

    return cost
arr=list(map(int,input().split()))
print(ElementsRemoval(arr))

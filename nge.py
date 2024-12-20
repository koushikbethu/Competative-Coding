def function(arr):
    stack = []
    nge = [-1] * len(arr)

    for i in range(len(arr)):
        while stack and arr[i] > arr[stack[-1]]:
            index = stack.pop()
            nge[index] = arr[i]
        stack.append(i)
    
    return nge

arr = list(map(int, input("Enter elements separated by space: ").split()))

result = function(arr)

print("Array:", arr)
print("Next Greatest Elements:", result)

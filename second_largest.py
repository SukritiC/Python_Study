if __name__ == '__main__':
    n = int(input())
    arr1 = map(int, input().split())
    arr = []
    for i in arr1:
        arr.append(i)
    mx = max(arr)
    s_mx = min(arr)
    
    for i in range(0,n):
        if arr[i] > mx:
            s_mx = mx
            mx = arr[i]
        elif arr[i] > s_mx and mx != arr[i]:
            s_mx = arr[i]
        
    print(s_mx)
    
n =int(input("nhap n= "))
def timidbaihat(n):
    result =[]
    arr = []
    count =0
    
    for i in range (n):
        x = input(f"input item[{i}]: ")
        arr.append(int(x))
    print(arr)
    for i in arr:
        if i not in result:
            result.append(i)
            count+=1
    return count,result
print(timidbaihat(n))
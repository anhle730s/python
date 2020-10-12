#bài 1.a tinh tong cua mang 1 chieu
#def tinh_tong(arr):
n = int(input("nhap n= "))
def tong(n):
    arr = [] 
    tong = 0 
    for i in range (n):
        x = input(f"input item[{i}]: ")
        arr.append(int(x))
        tong+=arr[i]
    return tong
print("tinh tong cac phan tu trong mang " ,tong(n))
#bài 1.b tinh tich cua mang 1 chieu
def tich(n):
    arr = [] 
    tich = 1
    for i in range (n):
        x = input(f"input item[{i}]: ")
        arr.append(int(x))
        tich*=arr[i]
    return tich
print("tinh tich cac phan tu trong mang la: ",tich(n))
#bài 1.c tim gia tri lon nhat
def max(n):
    arr = []
    
    for i in range (n):
        x = input(f"input item[{i}]: ")
        arr.append(int(x))
    ma = arr[0]
    for i in range (1, len(arr)):
        if(arr[i] > ma):
            ma=arr[i]
    return ma
print("so lon nhat trong mang la: ",max(n))
#bài 1.d tim gia tri nho nhat
def min(n):
    arr = []
    
    for i in range (n):
        x = input(f"input item[{i}]: ")
        arr.append(int(x))
    min=arr[0]
    for i in range (1, len(arr)):
        if(arr[i] < min):
            min = arr[i]
    return min
print("so nho nhat trong mang la: ",min(n))
#bài 1.e tìm các số lẻ trong mảng
def sole(n):
    result = []
    arr = []
    
    for i in range (n):
        x = input(f"input item[{i}]: ")
        arr.append(int(x))
    for i in range(0,len(arr)):
        if ( arr[i] % 2 != 0 ):
            result.append(arr[i])
    return result
print("cacso le trong mang la: ",sole(n))
 #bài 1.f tim cac so shan trong mang
def sochan(n):
    result = []
    arr = []
    
    for i in range (n):
        x = input(f"input item[{i}]: ")
        arr.append(int(x))
    for i in range(0,len(arr)):
        if ( arr[i] % 2 == 0 ):
            result.append(arr[i])
    return result
print("cac so chan trong mang la: ",sochan(n))
               
    



    
        

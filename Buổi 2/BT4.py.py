#4.	Tính tổng các số LẼ nằm trong đoạn từ 0 đến N
n =int(input('nhap n= '))
le=0
for i in range (0,n+1):
    if(i % 2 !=0 ):
        le +=i
        print (i)
    else:
        print()
print("tong cac so le ", le)
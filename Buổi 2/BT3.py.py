#3.	Tính tổng các số CHẴN nằm trong đoạn từ 0 đến N
n= int(input('nhap n = '))
chan=0
for i in range (0,n+1):
    if( i % 2 ==0 ):
        chan += i
        print (i)  
    else:
        print()
print("tong cac so chan ", chan)

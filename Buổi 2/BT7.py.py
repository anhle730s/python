#7.	Tính tổng giá trị từ 1 đến N, riêng số 17 thì bỏ qua
n= int(input('nhap n= '))
tong= 0
for i in range (1,n+1):
    if(i == 17):
        continue
         
    else:
        tong += i
        print(i, tong)
print (tong)
    

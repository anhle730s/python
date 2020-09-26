#6.	Tính tổng giá trị từ 1 đến N, nếu chạy đến số 13 thì không chạy nữa và xuất kết quả
n = int(input('nhap n= '))
tong = 0
for i in range (1,n+1):
    if (i == 13 ):
        break
    else:
        tong += i
        print(i, tong)
print (tong)
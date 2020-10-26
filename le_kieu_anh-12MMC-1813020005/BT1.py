# đề 1 
#Bài 1: Viết chương trình để xóa bỏ ký tự thứ m trong chuỗi không rỗng, với m là số không âm, nhập từ bàn phím.
m = int(input("nhap m= "))
chuoi=str(input("nhap chuoi: "))
for i in range (m):
    if (chuoi[i] == m):
      chuoi[i] == ''
      print(chuoi[i])
      
 


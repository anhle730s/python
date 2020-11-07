#Bài 10.3 Viết chương trình đọc một danh sách các số được ghi trong một tập tin văn bản, với mỗi số cách nhau bằng dấu khoảng trắng. Hiển thị danh sách ra màn hình và tính tổng các số đó.
f = open("test2.txt" ,'r' , encoding='utf-8' )
a=f.read()
print(a)
chuoi1=a.split(" ")
kq=0
for i in range (len(chuoi1)):
    kq=kq + float(chuoi1[i])
print("kết quả tổng các số trong danh sách: ",kq)
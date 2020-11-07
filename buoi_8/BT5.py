#Bài 10.5 Viết chương trình xóa một tập tin đang có trên hệ thống.
import os
chuoi=str(input("nhap chuoi: "))
if os.path.exists(chuoi):
    os.remove(chuoi)
    print("đã xóa tap tin ",chuoi)
else:
    print("khong tim thay tap tin  ",chuoi)

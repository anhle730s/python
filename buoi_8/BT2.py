#Bài 10.2 Viết chương trình đọc nội dung của một tập tin văn bản cho trước. Tên tập tin do người dùng chỉ định. Trong tập tin có nhiều dòng chữ.
f = open("test.txt" ,'r' , encoding='utf-8' )
a=f.read()
print(a)
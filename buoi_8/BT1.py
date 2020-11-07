# Bài 10.1 Viết chương trình tạo một tập tin văn bản với tên và nội dung do người dùng chỉ định.

a = open("abc.txt", 'w', encoding='utf-8')
a.write("hello word\n")
a.close()


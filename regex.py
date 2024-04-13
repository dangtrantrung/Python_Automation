import re

regex1=re.compile(r'anh (.*?) dep')
print(type(regex1))
chuoidemo='anh nghia hsgs dep trai dep'
kq=regex1.search(chuoidemo)
print(kq.group())
print(kq.group(1))
chuoidemo1='ngay dep troi, nang da gap anh nghia hsgs dep trai dep va nang da gap anh trung dep trai'
regex2=re.compile(r'gap (.*?) dep trai')
kq1=regex2.search(chuoidemo1)
print(kq1.group())
print("ket qua= "+kq1.group(1))
print(regex2.findall(chuoidemo1))
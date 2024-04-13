import re

regex1=re.compile(r'anh (.*?) dep')
print(type(regex1))
chuoidemo='anh nghia hsgs dep trai dep'
kq=regex1.search(chuoidemo)
print(kq.group())
print(kq.group(1))

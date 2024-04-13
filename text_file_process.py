import io
import os
from shutil import copyfile

print(os.getcwd())
os.chdir(r"E:\Python_Automation\thao tac file")
print(os.getcwd())
# f=open(".txt",'w')
# f.close()
# os.rename(".txt","file3.txt")
# copyfile("file1.txt","file4.txt")

# read file
# filename="file4.txt"
# f=open(filename,"a")
# line="anh trung dep trai"
# f.write(line +'\n')
# f.close()
# read,write file utf-8
filename="file4.txt"
f=open(filename,"a",encoding='utf-8')
line="anh trùng đẹp trai"
f.write(line +'\n')
f.close()

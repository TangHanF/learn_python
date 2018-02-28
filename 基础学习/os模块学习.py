import os

# os的access方法
print("是否存在：", os.access("I:/test.txt", mode=os.F_OK))
print("是否可读：", os.access("I:/test.txt", mode=os.R_OK))
print("是否可写：", os.access("I:/test.txt", mode=os.W_OK))
print("是否可执行：", os.access("I:/test.txt", mode=os.X_OK))

print("当前工作目录：", os.getcwd())
# 改变当前目录
os.chdir("I:/")
print("当前工作目录：", os.getcwd())

# 返回path指定的文件夹包含的文件或文件夹的名字的列表 不包含子文件夹、子文件
listdir = os.listdir("I:/learn_python/")
print(len(listdir))

# 　生成目录树结构
path = "I:/root"
for root, dirs, files in os.walk(path):
    level = root.replace(path, '').count(os.sep)
    indent = '\t' * 1 * level
    str_1 = '{}{}'.format(indent, os.path.basename(root)) + '\n'
    print(str_1, end="")
    sub_indent = '\t' * 1 * (level + 1)
    for f in files:
        str_2 = '{}{}'.format(sub_indent, f) + '\n'
        print(str_2, end="")

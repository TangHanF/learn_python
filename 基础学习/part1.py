"""
文件编码。Python3的源代码默认是utf-8编码，可以通过：
# -*- encoding:utf-8 -*-     进行设置
对于源码中存在中文的，建议在开头指定编码类型，防止乱码
"""
# -*- encoding:utf-8 -*-

# 列出Python3的关键字   自己在定义变量时不能使用其中的关键字。所有语言都是如此
import keyword

print("Python3的关键字有：", keyword.kwlist)

# 注释分为：单行注释（#）、多行注释（''' 或者 """）
# 这是单行注释
'''
这是多行注释，第一行
第二行
'''

# Python中 单引号和双引号没有区别，这个需要注意
str1 = '字符串'
str2 = "字符串"

print("str1类型：",type(str1))
print("str2类型：",type(str1))

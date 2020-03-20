#sql找前5，group之后
#正则匹配0.0.0.0
import re
s='kkk 192.137.1.336 kkk 1192.168.1.137 kk 192.168.1.138 kk'
l=re.findall(r'\b(?:25[0-5]\.|2[0-4]\d\.|[01]?\d\d?\.){3}(?:25[0-5]|2[0-4]\d|[01]?\d\d?)\b',s)
print(l)


l=re.findall(r'\b(?:(?:25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(?:25[0-5]|2[0-4]\d|[01]?\d\d?)\b',s)
print(l)

# '\b'表示符合要求的子串的第一个字符的前面和最后一个字符的后面不可以是'\w'字符（不可以是大小字母，数字，下划线）
#上述版本比较常用，但也存在一点问题：
s='kkk 192.137.1.336 kkk 192.168.1.137.123 kk 192.168.1.138 kk'
#第二个ip地址以'.'号作为分隔符，且每个数字在[0,255]之间，但该ip地址无效（多了一个数字）！！
l=re.findall(r'\b(?:25[0-5]\.|2[0-4]\d\.|[01]?\d\d?\.){3}(?:25[0-5]|2[0-4]\d|[01]?\d\d?)\b',s)
print(l)
['192.168.1.137', '192.168.1.138'] #将第二个ip地址，截取了前4个数字，但显然第二个ip地址本应是无效的！！
#
#

pa=re.findall(r'\b(?:25[0-5]\.|2[0-4]\d\.|[01]?\d\d?\.){3}(?:25[0-5]|2[0-4]\d|[01]?\d\d?)\b',s)
print(pa)
l=re.findall(r"^\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", s)
print(l)



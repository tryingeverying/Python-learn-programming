# import re

# '''findall:匹配字符串中所有符合要求的list'''
# lst = re.findall('\d+','我的电话是10086.我另外的电话是10001')  
# print(lst)

# '''finditer: 匹配字符串中所有符合要求内容，返回迭代器,从迭代器中获取内容用.group()方法'''
# it = re.finditer('\d+','我的电话是10086.我另外的电话是10001')
# for i in it:
#     print(i)
#     print(i.group())
    
# '''search() 返回的是match对象,且只获取第一个匹配对象,获取内容用.group()方法'''
# s = re.search('\d+','我的电话是10086.我另外的电话是10001')
# print(s)
# print(s.group())

# '''match,用法类似于search,但是默认从头匹配,相当于在正则表达式前面加了^'''
# m = re.search('\d+','m10006.我另外的电话是10001')
# print(m)
# print(m.group())
import re
s = """
<div class='joy'><span id='1'>郭麒麟</span></div>
<div class='bob'><span id='2'>宋轶</span></div>
<div class='john'><span id='3'>大聪明</span></div>
<div class='lily'><span id='4'>范思哲</span></div>
"""

obj = re.compile(r"<div class='.*?'><span id='\d+'>.*?</span></div>", re.S)

result = obj.finditer(s)
for it in result:
    print(it.group())









person = {'id':101, 'name':'disen', 'age':20}
person2 = {'id':101, 'age':30, 'sex':'男'}
person.update(person2)
person.setdefault('salary', 25)  # 如果key不存在，则添加，反之不添加
print(person)

# 一行代码实现字典的key和value互换
person = {value:key for key,value in person.items()}
print(person)

# 哪些类型可以作为key
# str, int, tuple
person.update({(101,'lovies'): ['打篮球','看小说']})
print(person)

from collections import OrderedDict
# help(OrderedDict)
od = OrderedDict()  # 有序字典， 按添加的先后顺序显示
od['a'] = '80'
od['c'] = 99
od['b'] = 109
# od.move_to_end('a')  # 将任意的key移动最后
print(od)

d = {}  
d['a'] = 80
d['c'] = 99
d['b'] = 109
print(d)

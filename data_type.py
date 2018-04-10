# 数据类型 一共有六种
# Number（数字） String（字符串）List（列表）Tuple（元组）Sets（集合）Dictionary（字典）
# 可变数据：List（列表）Dictionary（字典）
# bool是一种Number类型，这是与js不一样的地方，True和False是python3中的关键字，既然是数字类型就是可以与数字相加减
b = True
print(b + 1)
d = 4 + 3j
print(type(1), type(5.5), type(b), type(4 + 3j))  # int float bool complex

# 判断数据类型除了type，还有isinstance
a = 111
print(isinstance(a, int))

# 那么isinstance 与 type有什么区别吗？

# String类型 可以截取字符串，特别灵活。 str[2:]：字符串2到最后一个字符
# str * 2：连续输出字符串两次

# 序列list[]，可包含不同类型的； tuple元组(),也可包含不同类型，不过不能修改；
# set{}集合是无序不重复的序列，可以用来剔除重复元素，和测试成员关系 set也可以进行集合运算
student = {'Tom', 'Jim', 'Mary', 'Tom', 'Jack', 'Rose'}
# 剔除了重复的Tom元素
print(student)
print(type(student))
# 成员关系
if 'Rose' in student:
    print('Rose in student set')
else:
    print('Rose not in student set')

# 字典 dictionary, 类似于js中的对象，dict有丰富的内置函数keys(),values()
dict = {'name': 'luoqian', 'age': 22}
print(dict)
print(dict['name'])
print(dict.keys())
print(dict.values())


# 问题1.1
# 现在有一个包含 N 个元素的元组或者是序列，怎样将它里面的值解压后同时赋值给 N 个变量？
name, age = ('luoqian', 23)
print(name, age)

sex, nickname = ['man', 'luoq']
print(sex)
print(age)

# 解答
# 任意可迭代对象都可以同时赋值变量，只要是变量数量一致，如果不一致会报错。但是有时候你只需要其中某些值，可以使用占位符
data = [51, 81, 91, 101]
# 需要保证 _ 这个占位符不在其他地方使用
_, share, _, price = data
print(share, price)


# 问题1.2
# 从上一个问题衍生出：可迭代对象赋值多个变量，如果可迭代对象数量超过变量对象会报错valueerror，那么怎样才能从这个可迭代对象中解压出n个对象吗？
# starred expression 星号表达式
a, *b, c = range(5)
print(a)
print(b)
print(c)


grades = range(10)


def drop_first_last(grades):
    first, *middle, last = grades
    return (middle)


print(drop_first_last(grades))
sales_record = range(8)
*seven, last_month = sales_record
print(sum(seven))

records = [
    ('foo', 1, 2),
    ('bar', 'hello'),
    ('foo', 3, 4),
]


def do_foo(x, y):
    print('foo', x, y)


def do_bar(s):
    print('bar', s)

# *args 可以代表可变长度的元组


for tag, *args in records:
    print("*args")
    print(*args)
    if tag == 'foo':
        do_foo(*args)
    elif tag == 'bar':
        do_bar(*args)


# 字符串操作
line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
uname, *fields, homedir, sh = line.split(':')


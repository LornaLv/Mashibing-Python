# Date: 2023/2/19 下午8:22
# 格式化字符串
print('-----------第一种方式：使用%作为占位符------------')
name = '张三'
age = 20
print('我叫%s，今年%d岁了' % (name, age))

print('-----------第二种方式：使用{}作为占位符------------')
print('我叫{0}，今年{1}岁'.format(name,age))

print('-----------第三种方式：f-string------------')
print(f'我叫{name}，今年{age}岁')
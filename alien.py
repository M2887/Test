
#更新值的内容（或者说更改字典的键的属性）
'''
alien_0 ={}
alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0['color'])
print(alien_0['points'])

new_points = alien_0['points']
print("你获得了" + str(new_points) + "分")
alien_0['x_position'] = 0
alien_0['y_position'] = 25

print(alien_0)
alien_0['color'] = 'yellow'
print(alien_0)
'''

#下面是针对书上的外星人坐标位置更新练习
'''
alien_0 = {'x_position':0, 'y_position':25, 'speed':'medium'}
print("初始X坐标：" + str(alien_0['x_position']))

alien_0['speed'] = 'fast'

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    #这个外星人的速度一定很快
    x_increment =3

alien_0['x_position'] = alien_0['x_position'] + x_increment

print("新的X坐标为：" + str(alien_0['x_position']))
'''

#删除字典中的键值对
'''
alien_0 = {'color':'green', 'point':5}
print(alien_0)

del alien_0['point']
print(alien_0)
'''

'''
alien_0 = {
	'color':'green',
	'point':5,
	}
#遍历字典
for key, value in alien_0.items():
	print("\nKey:" + key.title())
	print("Value:" + str(value))
'''

#遍历所有键

alien_0 = {
	'color':'green',
	'point':5,
	}
color = ['green', 'red', 'bule']
for key in alien_0.keys():
	print(key)

    if key in color:
        print("你的颜色和" + key + "重叠了")

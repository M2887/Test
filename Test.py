from http import server
import random


'''
def hello(name):
        print('hello ' + name)
    hello('Alice')
    hello('Bob')

def getAnswer(answerNumber):
    if answerNumber == 1:
        return 'It is certain'
    elif answerNumber == 2:
        return 'It is decidedly so'
    elif answerNumber == 3:
        return 'yes'
    elif answerNumber == 4:
        return 'Reply hazy try again'
    elif answerNumber == 5:
        return 'ask again later'
    elif answerNumber == 6:
        return 'connectrate and ask again'
    elif answerNumber == 7:
        return 'my reply is no'
    elif answerNumber == 8:
        return 'Outlook not so good'
    elif answerNumber == 9:
        return 'Very doubtful'

print(getAnswer(random.randint(1,9)))

print('Hello', end='')
print("World")

def spam():
    print(eggs)
eggs = 333
spam()

def spam(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print('Error: Invalid argument.')

print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))

def spam(divideBy):
    return 42 / divideBy
try:
    print(spam(2))
    print(spam(12))
    print(spam(0))
    print(spam(1))
except ZeroDivisionError:
    print('Error: Invalid argument.')

secretNumber = random.randint(1,20)
print("猜猜我在想1~20中哪一个数字")
for guessNumber in range(1,7):
    print("请输入数字")
    guess = int(input())
    if guess < secretNumber:
        print("猜错了，要比这个数大")
    elif guess > secretNumber:
        print("猜错了，要比这个数小")
    else: 
        break
if guess == secretNumber:
    print("恭喜你猜对了,我想的数字是 "+ str(guess))
else:
    print("我想的数字是 "+str(secretNumber))
'''
'''
def collatz(number):
    if number % 2 == 0:
        return number//2
    else:
        return number * 3 + 1 
try:
    input_number = int(input("请输入一个整数: "))
    while True:
        print(collatz(input_number))
        input_number = collatz(input_number)
        if input_number == 1:
            break
except:
    print("请输入一个正整数")
'''
'''
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print("卧槽" + magician + "这表演也太叼了")
    print(magician + "我很期待你的下一次表演\n")
print("感谢每位魔术师给我们带来的精彩表演")

food = ['鸡公煲', '麻辣香锅', '冒菜', '辣子鸡']
for mylove in food:
    print(mylove)
    print("我可太喜欢吃 " + mylove + "了"  + '\n')
print("我真的非常喜欢吃辣的东西")

#创建数字列表
#使用函数range()
for value in range(1,5):
    print(value)
 
number = list(range(1,100,5))
print(number)
'''
'''   
s = []
for value in range(1,11):
    s.append(value**2)
print(s)
'''
'''
def point(alien_color):
    try:
        if alien_color == 'green':
            print("你因为射杀绿色外星人获得5分")
        elif alien_color == 'yellow':
            print("你获得10个点数")
        elif alien_color == 'red':
            print("你获得15点数")
        else:
            print("请输入正确的颜色")
    except:
        print("请输入字符")
alien_color = input("请输入你射杀的外星人颜色\n")
point(alien_color)    
'''
'''
age = []
if age:
    print('1')
else:
    print('2')
    '''
'''
user = ['admin', '111', '222', '333', '444']
current_user = ['aaa', 'bbb', 'ccc', 'ddd', 'eee']
new_user = ['AAA', 'aaa', 'bbb', 'BBB','CCC']
if user:
    print("接下来将对登录用户进行欢迎")
else:
    print("我们需要创建一个用户")

for login_user in user:
    if login_user == 'admin':
        print("你好管理员，要查看最近的报告吗")
    else:
        print(login_user + "欢迎登录XXX网站\n")   

for check_user in new_user:
    if check_user.upper() in current_user:
        print("不好意思，" + check_user +"这个名字已经存在了，麻溜点输点别的")
    else:
        print("恭喜你, " + check_user + "这个名字没有被人取过")    

d = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for d1 in d:
    print(d1)
    if d1 == 1:
        print('1st\n')
    elif d1 == 2:
        print('2nd\n')
    elif d1 == 3:
        print('3rd\n')
    elif d1 == 4:
        print('4th\n')
    elif d1 == 5:
        print('5th\n')
    elif d1 == 6:
        print('6th\n')
    elif d1 == 7:
        print('7th\n')
    elif d1 == 8:
        print('8th\n')
    else:
        print('9th\n')
'''


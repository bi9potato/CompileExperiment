
from sys import exit

vt_num = 6
vn_num = 5

from queue import LifoQueue
stack = LifoQueue(maxsize = 0)
inputStack = LifoQueue(maxsize = 0)
vn = ['E', 'e', 'T', 't', 'F']
vt = ['i', '+', '*', '(', ')', '#']
M =  [[1,0,0,1,0,0],[0,2,0,0,3,3],[4,0,0,4,0,0],[0,6,5,0,6,6],[8,0,0,7,0,0]]

def error():
    print('Error!')
    exit(1)

def JudeCharacter(str, i):
    return True if ((str[i] >= 'a' and str[i] <= 'z') or
                    (str[i] >= 'A' and str[i] <= 'Z') or
                    str[i] == '_') else False

def JudeCharacterOrNumber(str, i):
    return True if ((str[i] >= 'a' and str[i] <= 'z') or
                    (str[i] >= 'A' and str[i] <= 'Z') or
                    (str[i] >= '0' and str[i] <= '9') or
                    str[i] == '_') else False

# 预处理：变量/常量/数字（包括小数） 翻译为 i
def preprocessing(temp):
    formula = ''
    word = ''
    i = 0
    num = 0
    while (i < len(temp)):
        # 标识符
        if (i < len(temp) and JudeCharacter(temp, i)):
            word += temp[i]
            i += 1
            while (i < len(temp) and JudeCharacterOrNumber(temp, i)):
                word += temp[i]
                i += 1
            formula += 'i'
            word = ''
        # number
        elif (i < len(temp) and temp[i] >= '0' and temp[i] <= '9'):
            num = ord(temp[i]) - ord('0') + num * 10
            i += 1
            while (i < len(temp) and ((temp[i] >= '0' and temp[i] <= '9') or temp[i] == '.')):
                if (temp[i] != '.'):
                    num = ord(temp[i]) - ord('0') + num * 10
                    i += 1
                else:
                    num = str(num)
                    num += '.'
                    i += 1
                    while (i < len(temp) and temp[i] >= '0' and temp[i] <= '9'):
                        num += temp[i]
                        i += 1
                    break
            formula += 'i'
            num = 0
        # unary operators
        elif (i < len(temp) and
              temp[i] == '+' or
              temp[i] == '*' or
              temp[i] == '(' or
              temp[i] == ')' or
              temp[i] == '#'):
            formula += temp[i]
            i += 1
    # print(formula)#观察是否翻译正确
    return formula

def initial():
    stack.put('#')
    stack.put('E')
    temp = input('请输入你希望检查的公式（以#结尾）:')
    formula = preprocessing(temp)#翻译后的句子
    #逆序入栈
    for i in range(len(formula)-1, -1, -1):
        inputStack.put(formula[i])

def check_exist(X, arr):
    flag = -1
    for i in range(0, len(arr), 1):
        if(X == arr[i]): flag = i
    return flag

# Start
initial()
flag = True
a = inputStack.get();

while(flag):
    x = stack.get()
    if(check_exist(x, vt) > -1):
        if x == a:
            if x == '#':
                flag = False
            else:
                if(inputStack.empty()):
                    print('少#!',end = '')
                    error()
                else:
                    a = inputStack.get()    #输入栈指针后移

        else:
            error()
    else:
        case = M[check_exist(x, vn)][check_exist(a, vt)]
        if(case == 1):
            stack.put('e')
            stack.put('T')
            print('1', end='')
        elif(case == 2):

            stack.put('e')
            stack.put('T')
            stack.put('+')
            print('2', end='')
        elif (case == 3):

            print(3, end='')
        elif (case == 4):

            stack.put('t')
            stack.put('F')
            print(4, end='')
        elif (case == 5):

            stack.put('t')
            stack.put('F')
            stack.put('*')
            print(5, end='')
        elif (case == 6):

            print(6, end='')
        elif (case == 7):

            stack.put(')')
            stack.put('E')
            stack.put('(')
            print(7, end='')
        elif (case == 8):

            stack.put('i')
            print(8, end='')
        elif (case == 0):
            error()
print()
print('Success!')








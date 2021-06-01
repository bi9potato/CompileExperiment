
from sys import exit


global formula
global index
global sym

def scaner():
    global sym
    global index
    sym = transform(formula[index])
    # sym = formula[index]
    index += 1

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
    print(formula)#观察是否翻译正确
    return formula

def transform(a):
    if (a == '+' or a == '*' or a == '(' or a == ')' or a == '#'):
        print(end='')
    elif(len(a) == 0):# 少#
        a = ''
    elif ((ord(a) >= ord('1') & ord(a) <= ord('9')) or
          (ord(a) >= ord('a') & ord(a) <= ord('z'))):
        a = 'i'
    return a

def error():
    print('该字符串不符合语法规则')
    exit(1)

def E():
    T()
    E_()
    # print('E')

def E_():
    global sym
    if(sym == '+'):
        scaner()
        T()
        E_()
    # print('E_')

def T():
    F()
    T_()
    # print('T')

def T_():
    global sym
    if(sym == '*'):
        scaner()
        F()
        T_()
    # print('T_')

def F():
    global sym
    if(sym == 'i'):
        scaner()
    elif(sym == '('):
        scaner()
        E()
        if(sym == ')'):
            scaner()
        else:
            print('少)')
            error()
    else:
        print('缺少一个因子i')
        error()
    # print('F')


# Start
while(True):
    index = 0

    temp = input('请输入要判断的公式（以#结尾）:')
    temp = preprocessing(temp)
    formula = ['']*99       #定长list,防止list溢出
    i = 0
    for char in temp:
        formula[i] = char
        i += 1

    scaner()

    E()

    if(sym == '#'):
        print('success')
    else:
        print('少#！',end=' ')
        error()








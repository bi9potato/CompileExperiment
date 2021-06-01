
#%% file
with open('test01.txt', 'r') as f:
    text01 = f.read()

doc = open('汇编.txt','w')

#%% Stack
from Stack import MyStack
sp1 = MyStack()
sp2 = MyStack()
sp3 = MyStack()
sp1.push(0)
sp2.push('#')
sp3.push('-')

#%% 状态表 statetable
import numpy as np
statetable = np.array([[-1, -1, -1, -1, -1, -1, -1, -1, 2, -1, 1, -1],
                      [-1, -1, -1, -1, -1, -1, -1, -1, -1, -2, -1, -1],
                      [3, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
                      [-1, 5, -1, -1, -1, -1, 6, -1, 7, -1, -1, 4],
                      [-1, -1, 8, 9, 10, 11, -1, -1, -1, 101, -1, -1],
                      [-1, 5, -1, -1, -1, -1, 6, -1, 7, -1, -1, 12],
                      [-1, 5, -1, -1, -1, -1, 6, -1, 7, -1, -1, 13],
                      [-1, -1, 108, 108, 108, 108, -1, 108, -1, 108, -1, -1],
                      [-1, 5, -1, -1, -1, -1, 6, -1, 7, -1, -1, 14],
                      [-1, 5, -1, -1, -1, -1, 6, -1, 7, -1, -1, 15],
                      [-1, 5, -1, -1, -1, -1, 6, -1, 7, -1, -1, 16],
                      [-1, 5, -1, -1, -1, -1, 6, -1, 7, -1, -1, 17],
                      [-1, -1, 102, 102, 102, 102, -1, 102, -1, 102, -1, -1],
                      [-1, -1, 8, 9, 10, 11, -1, 18, -1, -1, -1, -1],
                      [-1, -1, 103, 103, 10, 11, -1, 103, -1, 103, -1, -1],
                      [-1, -1, 104, 104, 10, 11, -1, 104, -1, 104, -1, -1],
                      [-1, -1, 105, 105, 105, 105, -1, 105, -1, 105, -1, -1],
                      [-1, -1, 106, 106, 106, 106, -1, 106, -1, 106, -1, -1],
                      [-1, -1, 107, 107, 107, 107, -1, 107, -1, 107, -1, -1]])
#%% 规约
global num
global NXQ
NXQ = 0
doc = open("汇编.txt", 'w+')

def state_fuction(state):
    global NXQ
    global i
    global num

    if state == 0: # 用不到这个状态
        sp1.push(state)
        sp2.push(text01[i])
        sp3.push('_')
    elif state == 1:
        sp1.push(state)
        sp2.push(text01[i])
        sp3.push('_')
    elif state == 2:
        sp1.push(state)
        sp2.push('i')
        if word != '':
            sp3.push(word)
        else:
            sp3.push(num)
    elif state == 3:
        sp1.push(state)
        sp2.push('=')
        sp3.push('_')
    elif state == 5:
        sp1.push(state)
        sp2.push('@')
        sp3.push('_')
    elif state == 6:
        sp1.push(state)
        sp2.push('(')
        sp3.push('_')
    elif state == 7:
        sp1.push(state)
        sp2.push('i')
        if word != '':
            sp3.push(word)
        else:
            sp3.push(num)
    elif state == 8:
        sp1.push(state)
        sp2.push('+')
        sp3.push('_')
    elif state == 9:
        sp1.push(state)
        sp2.push('-')
        sp3.push('_')
    elif state == 10:
        sp1.push(state)
        sp2.push('*')
        sp3.push('_')
    elif state == 11:
        sp1.push(state)
        sp2.push('/')
        sp3.push('_')
    elif state == 18:
        sp1.push(state)
        sp2.push(')')
        sp3.push('_')

    elif state == 101:
        sp1.pop()
        sp2.pop()
        num = sp3.pop()
        sp1.pop()
        sp2.pop()
        sp3.pop()
        sp1.pop()
        sp2.pop()
        sp3.pop()
        sp2.push('E')
        state = statetable[sp1.top(), 10]
        sp1.push(state)
        global NXQ;NXQ += 1
        # 四元式
        print('(', '=', ',', num, ',', "_", ',', 'ENTRY(i)', ')')
        # 汇编语句
        doc = open("汇编.txt", 'a')
        print('MOV',' ','R0',' ,',num, file=doc)
        print('MOV',' ','a',' ,','R0', file=doc)
        doc.close()

        print('success')

    # E->-E
    elif state == 102:
        sp1.pop()
        sp2.pop()
        num = sp3.pop()
        sp1.pop()
        sp2.pop()
        sp3.pop()
        sp2.push('E')
        state = statetable[sp1.top(), 11]
        sp1.push(state)
        NXQ += 1
        # 四元式
        print('(', '@', ',', num, ',', '_', ',', 'T'+str(NXQ), ')')
        # 汇编语句
        doc = open("汇编.txt", 'a')
        print('MOV', ' ', 'R0', ' ,', num ,file=doc)
        print('NEG', ' ', 'R0' ,file=doc)
        print('MOV', ' ', 'T'+str(NXQ), ' ,', 'RO' ,file=doc)
        doc.close()

        sp3.push('T' + str(NXQ))
        i -= 1
    # E->E+E
    elif state == 103:
        sp1.pop()
        sp2.pop()
        num1 = sp3.pop()
        sp1.pop()
        sp2.pop()
        sp3.pop()
        sp1.pop()
        sp2.pop()
        num2 = sp3.pop()
        sp2.push('E')
        state = statetable[sp1.top(), 11]
        sp1.push(state)
        NXQ += 1
        # 四元式
        print('(', '+', ',', num1, ',', num2, ',', 'T'+str(NXQ), ')')
        # 汇编语句
        doc = open("汇编.txt", 'a')
        print('MOV', ' ', 'R0', ' ,', num1 ,file=doc)
        print('MOV', ' ', 'R1', ' ,', num2 ,file=doc)
        print('ADD', ' ', 'R1', ' ,', 'R0' ,file=doc)
        print('MOV', ' ', 'T'+str(NXQ), ' ,', 'R1' ,file=doc)
        doc.close()

        sp3.push('T' + str(NXQ))
        i -= 1
    # E->E-E
    elif state == 104:
        sp1.pop()
        sp2.pop()
        num1 = sp3.pop()
        sp1.pop()
        sp2.pop()
        sp3.pop()
        sp1.pop()
        sp2.pop()
        num2 = sp3.pop()
        sp2.push('E')
        state = statetable[sp1.top(), 11]
        sp1.push(state)
        NXQ += 1
        # 四元式
        print('(', '-', ',', num1, ',', num2, ',', 'T'+str(NXQ), ')')
        # 汇编语句
        doc = open("汇编.txt", 'a')
        print('MOV', ' ', 'R0', ' ,' ,num1,file=doc)
        print('MOV', ' ', 'R1', ' ,', num2 ,file=doc)
        print('SUB', ' ', 'R1', ' ,', 'R0' ,file=doc)
        print('MOV', ' ', 'T'+str(NXQ), ' ,', 'R1' ,file=doc)
        doc.close()

        sp3.push('T' + str(NXQ))
        i -= 1
    # E->E*E
    elif state == 105:
        sp1.pop()
        sp2.pop()
        num1 = sp3.pop()
        sp1.pop()
        sp2.pop()
        sp3.pop()
        sp1.pop()
        sp2.pop()
        num2 = sp3.pop()
        sp2.push('E')
        state = statetable[sp1.top(), 11]
        sp1.push(state)
        NXQ += 1
        # 四元式
        print('(', '*', ',', num1, ',', num2, ',', 'T'+str(NXQ), ')')
        # 汇编语句
        doc = open("汇编.txt", 'a')
        print('MOV', ' ', 'AL', ' ,', num1 ,file=doc)
        print('MOV', ' ', 'CL', ' ,', num2 ,file=doc)
        print('MUL', ' ', 'CL' ,file=doc)
        print('MOV', ' ', 'T'+str(NXQ), ' ,', 'AX' ,file=doc)
        doc.close()

        sp3.push('T' + str(NXQ))
        i -= 1
    # E->E/E
    elif state == 106:
        sp1.pop()
        sp2.pop()
        num1 = sp3.pop()
        sp1.pop()
        sp2.pop()
        sp3.pop()
        sp1.pop()
        sp2.pop()
        num2 = sp3.pop()
        sp2.push('E')
        state = statetable[sp1.top(), 11]
        sp1.push(state)
        NXQ += 1
        # 四元式
        print('(', '/', ',', num1, ',', num2, ',', 'T'+str(NXQ), ')')
        # 汇编语句
        doc = open("汇编.txt", 'a')
        print('MOV', ' ', 'AX', ' ,', num1 ,file=doc)
        print('MOV', ' ', 'CL', ' ,', num2 ,file=doc)
        print('DIV', ' ', 'CL' ,file=doc)
        print('MOV', ' ', 'T'+str(NXQ), ' ,', 'AL' ,file=doc)
        doc.close()

        sp3.push('T' + str(NXQ))
        i -= 1
    # E->(E)
    elif state == 107:
        sp1.pop()
        sp2.pop()
        sp3.pop()
        sp1.pop()
        sp2.pop()
        num = sp3.pop()
        sp1.pop()
        sp2.pop()
        sp3.pop()
        #
        sp2.push('E')
        state = statetable[sp1.top(), 11]
        sp1.push(state)
        sp3.push(num)
        i -= 1
    # E->i
    elif state == 108:
        sp1.pop()
        sp2.pop()
        num = sp3.pop()
        sp2.push('E')
        state = statetable[sp1.top(), 11]
        sp1.push(state)
        sp3.push(num)
        i -= 1


    # print('state==', state)
    # print(sp1.top(), end=' ')
    # print(sp2.top(), end=' ')
    # print(sp3.top())
#%%
word = ''       # identifier | ReservedWord
global i;i = 0  # index of program
num = 0         # number
operator = ''   # operator
bracket = ''    # brackets

def JudeCharacter():
    return True if ((text01[i] >= 'a' and text01[i] <= 'z') or
                    (text01[i] >= 'A' and text01[i] <= 'Z') or
                     text01[i] == '_') else False

def JudeCharacterOrNumber():
    return True if ((text01[i] >= 'a' and text01[i] <= 'z') or
                    (text01[i] >= 'A' and text01[i] <= 'Z') or
                    (text01[i] >= '0' and text01[i] <= '9') or
                     text01[i] == '_') else False

# main
while (i < len(text01)):
    # i point the last character of current word/number, and i++ in the end of the circle

    # identifier
    if (JudeCharacter()):
        word += text01[i]
        i += 1
        while (JudeCharacterOrNumber()):
            word += text01[i]
            i += 1

        state = statetable[sp1.top(), 8]
        state_fuction(state)

        word = ''
        i -= 1

    # integer
    elif (text01[i] >= '0' and text01[i] <= '9'):
        num = 0 # 清零

        num = ord(text01[i]) - ord('0') + 10 * num
        i += 1
        while ((text01[i] >= '0' and text01[i] <= '9') or text01[i] == '.'):
            if(text01[i] != '.'): #integer
                num = ord(text01[i]) - ord('0') + num * 10
                i += 1
            else: # float
                num = str(num)
                num += '.'
                i += 1
                while (text01[i] >= '0' and text01[i] <= '9'):
                    num += text01[i]
                    i += 1
                break

        if text01[i] == '.': # 不能有2个以上.
            print('错误。float不允许有2个及以上‘.’符号，请检查表达式')
            exit(-1)

        state = statetable[sp1.top(), 8]
        state_fuction(state)

        i -= 1 # rollback pointer

    # unary operators
    elif (text01[i] == '+' or
          text01[i] == '-' or
          text01[i] == '*' or
          text01[i] == '/' or
          text01[i] == ':' or
          text01[i] == ';' or
          text01[i] == ','):

        if text01[i] == '+':
            j = 2
        elif text01[i] == '-':
            j = 3
        elif text01[i] == '*':
            j = 4
        elif text01[i] == '/':
            j = 5

        # print('j=',j)
        state = statetable[sp1.top(), j]
        state_fuction(state)

    # unary or binary operators
    elif (text01[i] == '=' or
          text01[i] == '<' or
          text01[i] == '>' or
          text01[i] == '!'):
        operator += text01[i]
        i += 1
        if (text01[i] == '='): # ==
            operator += text01[i]
        else:

            if text01[i-1] == '=':
                j = 0
            state = statetable[sp1.top(), j]
            state_fuction(state)

            i -= 1  # rollback index
        operator = ''
    elif (text01[i] == '&'):
        operator += text01[i]
        i += 1
        if (text01[i] == '&'):
            operator += text01[i]
        else:
            i -= 1  # rollback index
        operator = ''
    elif (text01[i] == '|'):
        operator += text01[i]
        i += 1
        if (text01[i] == '|'):
            operator += text01[i]
            i -= 1  # rollback index
        operator = ''

    # brackets
    # need to be improved
    # loss judgement of right bracket
    elif (text01[i] == '(' or
          text01[i] == '[' or
          text01[i] == '{'):
        bracket = text01[i]

        state = statetable[sp1.top(), 6]
        state_fuction(state)

    elif (text01[i] == ')' or
          text01[i] == ']' or
          text01[i] == '}'):
        bracket = text01[i]

        state = statetable[sp1.top(), 7]
        state_fuction(state)

    elif (text01[i] == '@'):
        state = statetable[sp1.top(), 1]
        state_fuction(state)

    # end
    elif (text01[i] == '#'):
        state = statetable[sp1.top(), 9]
        if state_fuction(state) == -2:
            break

    i += 1

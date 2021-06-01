import numpy as np

precede_stable = np.array([['>', '<', '<', '>', '<', '>'],
                           ['>', '>', '<', '>', '<', '>'],
                           ['<', '<', '<', '=', '<', ''],
                           ['>', '>', '', '>', '', '>'],
                           ['>', '>', '', '>', '', '>'],
                           ['<', '<', '<', '', '<', '=']])
print(precede_stable)
# Stack
from Stack import MyStack
# 报错
from sys import exit


# %% p判断数字

# %% 计算
def Calculate(operand_stack, operator_stack):
    num2 = float(operand_stack.pop())  # 后入栈的是第二个操作数
    num1 = float(operand_stack.pop())  # 先入栈的是第一个操作数
    op = operator_stack.pop()
    if (op == '+'):
        num1 = num1 + num2
    elif (op == '-'):
        num1 = num1 - num2
    elif (op == '*'):
        num1 = num1 * num2
    elif (op == '/'):
        num1 = num1 / num2
    return num1


# %% main
#
num = ''
#
operator_stack = MyStack()  # 运算符栈
operand_stack = MyStack()  # 操作数栈
operator_stack.push('#')

#
formula = input('请输入算数表达式（以#结尾）：')
while (not formula.endswith('#')):
    print('少#,请重新输入')
    formula = input('请输入算数表达式（以#结尾）：')
#
i = 0
flag = True
while (flag):
    if (operator_stack.top() == '#' and formula[i] == '#'):
        print('结果为：', operand_stack.pop())
        break
    elif (formula[i] >= '1' and formula[i] <= '9'):  # 数字以1-9开头
        num += formula[i]
        i += 1
        while ((formula[i] >= '0' and formula[i] <= '9') or formula[i] == '.'):
            num += formula[i]
            i += 1
        operand_stack.push(num)
        num = ''
    elif (formula[i] == '0'):  # 数字不能以0开头
        i += 1
        if (formula[i] >= '1' and formula[i] <= '9'):  # 0的下一个是否是数字？
            print('数字不允许以0开头')
            flag = False
            exit()
        else:
            operand_stack.push(0)

    elif (operator_stack.top() == '(' and formula[i] == ')'):
        operator_stack.pop()  # 弹出左括号
        i += 1  # 算式指针指向右括号下一个
    else:
        if (formula[i] == '+'):
            m = 0
        elif (formula[i] == '-'):
            m = 0
        elif (formula[i] == '*'):
            m = 1
        elif (formula[i] == '/'):
            m = 1
        elif (formula[i] == '('):
            m = 2
        elif (formula[i] == ')'):
            m = 3
        elif (formula[i] == '#'):
            m = 5
        else:
            m = 4

        if (operator_stack.top() == '+'):
            n = 0
        elif (operator_stack.top() == '-'):
            n = 0
        elif (operator_stack.top() == '*'):
            n = 1
        elif (operator_stack.top() == '/'):
            n = 1
        elif (operator_stack.top() == '('):
            n = 2
        elif (operator_stack.top() == ')'):
            n = 3
        elif (operator_stack.top() == '#'):
            n = 5
        else:
            n = 4

        if(precede_stable[n, m] == '<'):  # 左<右 op入op栈
            operator_stack.push(formula[i])
            i += 1
        elif (precede_stable[n, m] == '>'):  # 左>右 计算
            num1 = Calculate(operand_stack, operator_stack)
            operand_stack.push(num1)

    # 检错
    # print(operator_stack.top(), end=' ')
    # print(operand_stack.top())
    # 15.3+(2*3-(1.2+11)/2)#

print(num)

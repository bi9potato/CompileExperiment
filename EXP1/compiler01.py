

with open('test01.txt', 'r') as f:
    text01 = f.read()

with open('dictionary.txt', 'r', encoding='utf-8') as f:
    dic = {}
    for line in f.readlines():
        line = line.strip('\n')
        line = line.split(' ', 1)
        dic[line[0]] = line[1]
# print('main' in dic.keys())

word = ''       # identifier | ReservedWord
i = 0           # index of program
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


# main_function
while (i < len(text01)):
    # i point the last character of current word/number, and i++ in the end of the circle

    # identifier
    if (JudeCharacter()):
        word += text01[i]
        i += 1
        while (JudeCharacterOrNumber()):
            word += text01[i]
            i += 1
        print(word + ' ' + dic[word]) if (word in dic.keys()) else print(word + ' ' + dic['标识符'])
        word = ''
        i -= 1

    # number
    elif (text01[i] >= '0' and text01[i] <= '9'):
        num = ord(text01[i]) - ord('0') + num * 10
        i += 1
        while ((text01[i] >= '0' and text01[i] <= '9') or text01[i] == '.'):
            if(text01[i] != '.'):
                num = ord(text01[i]) - ord('0') + num * 10
                i += 1
            else:
                num = str(num)
                num += '.'
                i += 1
                while (text01[i] >= '0' and text01[i] <= '9'):
                    num += text01[i]
                    print(type(num))
                    i += 1
                break
        print(num, dic['实数']) if( '.' in str(num)) else print(num, dic['整数'])
        num = 0
        i -= 1

    # unary operators
    elif (text01[i] == '+' or
          text01[i] == '-' or
          text01[i] == '*' or
          text01[i] == '/' or
          text01[i] == ':' or
          text01[i] == ';' or
          text01[i] == ','):
        print(text01[i] + ' ' + dic[text01[i]])

    # unary or binary operators
    elif (text01[i] == '=' or
          text01[i] == '<' or
          text01[i] == '>' or
          text01[i] == '!'):
        operator += text01[i]
        i += 1
        if (text01[i] == '='):
            operator += text01[i]
            print(operator + ' ' + dic[operator])
        else:
            print(operator + ' ' + dic[operator])
            i -= 1  # rollback index
        operator = ''
    elif (text01[i] == '&'):
        operator += text01[i]
        i += 1
        if (text01[i] == '&'):
            operator += text01[i]
            print(operator + ' ' + dic[operator])
        else:
            print(operator + ' ' + dic[operator])
            i -= 1  # rollback index
        operator = ''
    elif (text01[i] == '|'):
        operator += text01[i]
        i += 1
        if (text01[i] == '|'):
            operator += text01[i]
            print(operator + ' ' + dic[operator])
            i -= 1  # rollback index
        operator = ''

    # brackets
    # need to be improved
    # loss judgement of right bracket
    elif (text01[i] == '(' or
          text01[i] == '[' or
          text01[i] == '{'):
        bracket = text01[i]
        print(bracket, dic[bracket])
    elif (text01[i] == ')' or
          text01[i] == ']' or
          text01[i] == '}'):
        bracket = text01[i]
        print(bracket, dic[bracket])

    i += 1
